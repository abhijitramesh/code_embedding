from jvm_embedding import *
import sys
import json
import gensim
import numpy as np
from sklearn.decomposition import TruncatedSVD,PCA

inpath = sys.argv[1]
vecpath = sys.argv[2]

if len(sys.argv) > 3:
    scale = float(sys.argv[3])
else:
    scale = 1.0

if len(sys.argv) > 4:
    post_processing = sys.argv[4]
    threshold_param = int(sys.argv[5])
else:
    post_processing = None
    threshold_param = None

def similarity(v1, v2):
    #return np.dot(v1, v2)
    return np.linalg.norm(v1 - v2)/scale

model = gensim.models.KeyedVectors.load_word2vec_format(vecpath, binary=False)

vectors = model.vectors
common_vector = np.mean(vectors,axis=0)
intermediate_vectors = vectors-common_vector

if post_processing=="SVD":
    svd = TruncatedSVD(threshold_param)
    postprocessed_vector = svd.fit(intermediate_vectors).components_
    postprocessed = intermediate_vectors - np.matmul(np.matmul(vectors,postprocessed_vector.T),postprocessed_vector)
    model.vectors = postprocessed
elif post_processing=="PCA":
    pca = PCA(threshold_param)
    postprocessed_vector = pca.fit(intermediate_vectors).components_
    postprocessed = intermediate_vectors - np.matmul(np.matmul(vectors,postprocessed_vector.T),postprocessed_vector)
    model.vectors = postprocessed

tf_dataset, df, n_methods = build_tf_df(inpath)

method_embeddings = {}
for path, method_features in tf_dataset.items():
    method_embeddings[path] = {}
    for  method in method_features.keys():
        feature_dict = method_features[method]
        method_embeddings[path][method] = sum(model[f]*v for f, v in feature_dict.items() if f in model)

for path1, method_features1 in tf_dataset.items():
    for method1, feature_dict1 in method_features1.items():
        print()
        print(path1, "@", method1, "vs: ")
        res = []
        for path2, method_features2 in tf_dataset.items():
                for method2, feature_dict2 in method_features2.items():
                    if path1 == path2 and method1 == method2:
                        continue
                    sim = similarity(method_embeddings[path1][method1], method_embeddings[path2][method2])
                    res.append( (path2 + " " + method2, sim))
        res.sort(reverse=False, key=lambda t: t[1])
        for target, sim in res:
            print("    ", target, ":", sim)

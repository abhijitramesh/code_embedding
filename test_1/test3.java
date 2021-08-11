public class test3 {
    int mul4(int y){
        return y * 4;
    }
    public int muldiv(int x){
        int i=0;
        while (i<3){
          x = x*4;
          i+=1;
        }
        test2 t = new test2();
        return t.div4(x);
    }

    public String concatdashString(String x,int n){
        String res = "";
        for (int i=0;i<n;i++){
            res += "_";
        }
        return res;
    }
}


class test4{
   int mn(int y){
	   return y * 3;
   }
    public int m(int x){
    	int i = 0;
    	while (true){
    		x = x + 3;
    		i += 1;
    		if( i > 3){
    			break;
    		}
    	}
	    test2 t = new test2();
	    return t.n(x);
    }

    public String m2(String x, int n){
      String res= "";
       for(int i=0;i<n;i++){
          res += x;
       }
       return res;
    }
}

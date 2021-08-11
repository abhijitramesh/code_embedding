public class test {
    int mul4(int y){
        return y * 4;
    }
    public int muldiv(int x){
        for(int i=0;i<3;i++)
            x = x * 4;
        test2 t = new test2();
        return t.div4(x);
    }
}

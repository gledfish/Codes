package learning.vehicle;

//卡车类继承交通工具
public class Truck extends vehicle  {
    private int cargocap;//货容量
    public Truck(int p, int f, int m, int c){
        super(p, f, m);
        c= cargocap;
    }
    //
    int getCarge(){
        return cargocap;
    }
    void putCargo(int c){
        cargocap = c;
    }
}
//java实例化对象时使用set方法还是构造器方法 ？
/*
 * 一般情况下，两种构造方法都要设置，构造器方法多用于起初第一次赋值，可以赋多个值，而set方法一次只能赋一个值，多用于补充赋值。
 */
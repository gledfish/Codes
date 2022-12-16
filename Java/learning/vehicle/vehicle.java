package learning.vehicle;
//交通工具类
public class vehicle {
    private int passengers;
    private int fuelcap; 
    private int mpg;

    public vehicle(int p, int f, int m){
        passengers = p;
        fuelcap = f;
        mpg = m;
    }
    //返回最大行程
    int range(){
        return mpg * fuelcap;
    }

    //返回一定路程的耗油量
    double fuelNeeded(int miles){
        return (double) miles / mpg;
    }
}

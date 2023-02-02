package Exercise;

import static java.lang.Math.PI;

/*
 * ClassName:CircleTest
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 20:20
 * @author:gled fish
 */
class Circle{
    double r;

    public double square() {
        double s =  r * r * PI;
        return s;
    }
}
public class CircleTest {
    public static void main(String[] args) {
        Circle c1 = new Circle();
        c1.r = 2.5;
        double s1 = c1.square();
        System.out.println(s1);
    }
}

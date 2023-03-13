package OOP;

import static java.lang.Math.PI;

/*
 * ClassName:Circle
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/3/12 - 20:34
 * @author:gled fish
 */
public class Circle extends GeometricObject{
    private double radius; //半径

    public Circle(String color, double weight, double radius) {
        super(color, weight);
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }
    @Override
    public double findArea(){
        return PI * radius * radius;
    }
}

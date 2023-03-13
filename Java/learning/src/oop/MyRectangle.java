package OOP;

/*
 * ClassName:MyRectangle
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/3/12 - 20:38
 * @author:gled fish
 */
public class MyRectangle extends GeometricObject{
    private double width, height; //宽和高

    public MyRectangle(String color, double weight, double width, double height) {
        super(color, weight);
        this.width = width;
        this.height = height;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    @Override
    public double findArea() {
        return width * width;
    }
}

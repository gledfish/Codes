package OOP;

/*
 * ClassName:GeometricObject
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/3/12 - 20:27
 * @author:gled fish
 */
public class GeometricObject {
    protected String color;
    protected double weight;
    protected GeometricObject(String color, double weight){
        this.color = color;
        this.weight = weight;
    }

    public String getColor() {
        return color;
    }

    public double getWeight() {
        return weight;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public double findArea() {
        return 0.0;
    }
}

package OOP;

/*
 * ClassName:GeometricTest
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/3/12 - 20:40
 * @author:gled fish
 */
public class GeometricTest {
    //比较面积是否相等
    public boolean equalsArea(GeometricObject g1, GeometricObject g2) {
        return g1.findArea() == g2.findArea();
    }

    //显示面积
    public void displayGeometricArea(GeometricObject g){
        System.out.println("面积为" + g.findArea());
    }

    public static void main(String[] args) {
        GeometricTest test = new GeometricTest();
        Circle c1 = new Circle("red", 1.0, 2.3);
        Circle c2 = new Circle("red", 1.0, 3.3);

        test.displayGeometricArea(c1);
    }
}

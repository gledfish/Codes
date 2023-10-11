package Exercise;
/*
 * ClassName:RectangleTest
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 20:36
 * @author:gled fish
 */
class Rectangle{
    int square;

    public void printRect(){
        //输出矩形
        for(int i = 0; i < 8; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print('*');

            }
            System.out.println();
        }
    }
    public int square(){
        int sum = 0;
        for(int i = 0; i < 8; i++) {
            for (int j = 0; j < 10; j++) {
                sum++;
            }
        }
        return sum;
    }
}
public class RectangleTest {
    public static void main(String[] args) {
        Rectangle R1 = new Rectangle();
        R1.printRect();
        R1.square();

    }
}

package OOP;

/*
 * ClassName:OverLoadTest
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/2/2 - 9:21
 * @author:gled fish
 */

/*
方法重载
1.同一个类中，允许存在一个以上的同名方法，只要参数个数不同，或者参数数据类型不同
    跟方法的权限修饰符，返回值类型，形参变量名无关
 */
class Overload {
    public void getSum(int i, int j) {
        System.out.println(i + j);
    }

    public void getSum(String i, int j) {
        System.out.println(i + j);
    }

//    public int getSum(int i, int j){
//        System.out.println(i + j);
//    }
//}
}
public class OverLoadTest {
    public static void main(String[] args) {
        Overload o1 = new Overload();
        o1.getSum(1,2);
        o1.getSum("1",2);

    }
    }


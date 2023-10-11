package OOP;

/*
 * ClassName:PhoneTest
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/2/2 - 9:06
 * @author:gled fish
 */

class Phone{
    double price;//价格

    public void sendEmail(){
        System.out.println("发送邮件");
    }

    public void playGame(){
        System.out.println("玩游戏");
    }


}
public class PhoneTest {
    public static void main(String[] args) {
        Phone p1 = new Phone();
        System.out.println(p1);

        p1.sendEmail();
        p1.playGame();

        //匿名对象
        //声明并一次性使用的对象
        //用途：作为参数传入方法，简化参数传入
        new Phone().sendEmail();
        new Phone().playGame();
    }
}

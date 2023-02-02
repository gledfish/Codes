package OOP;

/*
 * ClassName:CustomerTest
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 12:34
 * @author:gled fish
 */

/*
类中方法的声明和使用
类：描述类应该具有的功能

方法的声明：权限修饰符 返回值类型 方法名（形参列表）{
    方法体
}
方法的使用可以调用当前类的属性或方法

 */

class Customer{
    String name;
    int age;
    boolean isMale;

    public void eat(){
        System.out.println("吃饭");
    }
    public void sleep(int hour){
        System.out.println("休息了"+hour + "时间");
    }

    public String getName(){
        return name;
    }

    public String getNation(String nation) {
        String info = "我的国籍是" + nation;
        return info;
    }

}


public class CustomerTest {
    public static void main(String[] args) {
        Customer customer1 = new Customer();
        customer1.eat();
    }
}

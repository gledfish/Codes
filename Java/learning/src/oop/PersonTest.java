package OOP;/*
 * ClassName:Person
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 10:41
 * @author:gled fish
 */
class Person {
    //属性
    String name;
    int age = 1;
    boolean isMale;

    //方法
    public void eat(){
        System.out.println("吃饭");
    }
    public void sleep(){
        System.out.println("睡觉");
    }

    public void talk(String language){
        System.out.println("人可以说"+language);
    }

}
public class PersonTest {
    public static void main(String[] args) {
        //创建对象
        Person p1 = new Person();

        //调用对象的属性
        p1.name = "Tom";
        p1.isMale = true;
        System.out.println(p1.name);

        //调用对象的方法
        p1.eat();
        p1.sleep();
        p1.talk("English");

        Person p2 = new Person();
        //未赋值时，属性为默认值
        System.out.println(p2.name);//null
        System.out.println(p2.isMale);//false

//        将 p1 保存对象的地址赋值给 p3,导致 p3 和 p1 指向同一个地址
        Person p3 = p1;
        System.out.println(p3.name);//Tom
        p3.age = 10;
        System.out.println(p1.age);//10
    }
}

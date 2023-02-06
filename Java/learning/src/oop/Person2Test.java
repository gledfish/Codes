package OOP;

/*
 * ClassName:Person2Test
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/2/2 - 20:46
 * @author:gled fish
 */
class Person2{
/*    构造器的作用
    创建对象
    初始化属性
    如果没有显式的定义类的构造器，系统默认提供一个空参的构造器
    构造器不属于方法
    可以定义多个构造器，彼此构成重载
    如果用户自定义构造器，则不使用默认构造器构造器

    定义构造器的方法：
        权限修饰符 类名（形参列表）{}
*/
    String name;
    int age;

    //构造器
    public Person2(){
        System.out.println("Person2()");
    }

    public Person2(String name, int age){
        System.out.println(name);
    }
    public void eat(){
        System.out.println("eating");
    }

    public void study(){
        System.out.println("studying");
    }
}

public class Person2Test {
    public static void main(String[] args) {
        Person2 p = new Person2("gledfish", 19);
        p.eat();
        p.study();
    }
}

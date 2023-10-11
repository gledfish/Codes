package OOP;

/*
 * ClassName:AnimalTest2
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/3/10 - 9:13
 * @author:gled fish
 */
class Animal2{
    String name;
    int age;

    public void eat(){
        System.out.println("eating");
    }
}

class Cat extends Animal2 {
    int count; //a cat is able to catch a mouse

    public void catchMouse(){
        count++;
        System.out.println("a mouse died");
    }
}

//子类不能直接访问父类私有的成员变量
//但是可以通过 get/set 方法访问

// java不支持多重继承

public class AnimalTest2 {
    public static void main(String[] args) {
        Cat cat = new Cat();
        cat.name = "Tom";
        cat.age = 18;
        cat.eat();
        cat.catchMouse();

    }
}

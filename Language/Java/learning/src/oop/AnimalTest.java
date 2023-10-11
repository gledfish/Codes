package OOP;

/*
 * ClassName:AnimalTest
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/2/2 - 11:53
 * @author:gled fish
 */
class Animal {
    String name;
    int age;
    private int legs;

    public void setLegs(int legs) {
        if (legs >= 0) {
            this.legs = legs;
        }
    }
    public int getLegs() {
        return this.legs;
    }
    /*
    封装体现：将属性设置为私有，提供公有的方法来设置和获取属性。
     */
    public void eat(){
        System.out.println("eating");
    }

}
public class AnimalTest {
    public static void main(String[] args) {
        Animal a = new Animal();
        a.name = "小花";
        a.setLegs(4);
        System.out.println(a.getLegs());
    }
}

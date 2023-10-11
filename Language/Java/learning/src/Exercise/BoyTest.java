package Exercise;

class Boy {
    String name;
    int age;

    public Boy(String name, int age){
        this.name = name;
        this.age = age;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return this.name;
    }
    public void setAge(int i){
        this.age = i;
    }
    public int getAge() {
        return this.age;
    }

    public void marry(String name){
        System.out.println(this.name + "is married with" + name);
    }

    public void shout(){
        System.out.println("aaaaaaaa");
    }
}
/*
 * ClassName:BoyTest
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/2/6 - 19:17
 * @author:gled fish
 */
public class BoyTest {
    public static void main(String[] args) {
        Boy b1 = new Boy("gledfish", 18);
        System.out.println(b1.getAge());
    }
}

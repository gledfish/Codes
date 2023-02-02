package Exercise;
/*
 * ClassName:Person
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 10:41
 * @author:gled fish
 */
class Person {
    //属性
    String name;
    int age;
    int sex;

    //方法
    public void study(){
        System.out.println("studying");
    }
    public void showAge(){
        System.out.println("年龄为" + age);
    }
    public int addAge(int addedAge){
        age = age + addedAge;
        return age;
    }

}
public class PersonTest {
    public static void main(String[] args) {
        //创建对象
        Person p1 = new Person();

        //调用对象的属性
        p1.name = "Tom";
        p1.age = 20;
        p1.sex = 0;

        //调用对象的方法
       p1.study();
       p1.showAge();
       p1.addAge(2);
       p1.showAge();

    }
}

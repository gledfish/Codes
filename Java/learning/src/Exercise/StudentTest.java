package Exercise;

/*
 * ClassName:StudentTest
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 19:54
 * @author:gled fish
 */
class Student{
    //属性
    String name;
    int age;
    String major;
    String interest;

    //方法
    public void Say(){
        System.out.println("姓名：" + name);
        System.out.println("年龄：" + age);
        System.out.println("专业：" + major);
        System.out.println("兴趣：" + interest);
    }
}
public class StudentTest {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "gled fish";
        s1.Say();
    }
}

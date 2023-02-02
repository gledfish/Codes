package Exercise;

/*
 * ClassName:TeacherTest
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 19:59
 * @author:gled fish
 */class Teacher{
    //属性
    String name;
    int age;
    int teachAge;
    String course;

    //方法
    public void Say(){
        System.out.println("姓名：" + name);
        System.out.println("年龄：" + age);
        System.out.println("教龄：" + teachAge);
        System.out.println("课程：" + course);
    }
}
public class TeacherTest {
    public static void main(String[] args) {
        Teacher t1 = new Teacher();
        t1.name = "gled fish";
        t1.Say();
    }
}

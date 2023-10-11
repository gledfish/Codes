package Exercise;

/*
 * ClassName:StudentArray
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 21:18
 * @author:gled fish
 */

class student{
    int number;//学号
    int state;//年级
    int score;//分数
}
public class StudentArray {
    public static void main(String[] args) {
        student[] students = new student[20];
        for(int i = 0; i < students.length; i++){
            students[i] = new student();
            students[i].number = i + 1;
            students[i].state = (int)(Math.random() * 5 + 1);
            students[i].score = (int)(Math.random() * 100);
        }
        for (Exercise.student student : students) {
            System.out.println(student);
        }
    }
}

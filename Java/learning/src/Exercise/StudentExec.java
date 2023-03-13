package Exercise;

/*
 * ClassName:StudentExec
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/3/10 - 9:25
 * @author:gled fish
 */

class Person2 {
    String name;
    int age;
    char sex;

    void Person2(String name, int age, char sex) {
        this.name = name;
        this.age  = age;
        this.sex = sex;
    }
    String toString2() {
        return this.name + " " + this.age + " " + this.sex;
    }
}

class Student2 extends Person2 {
    long number;
    int math;
    int english;
    int computer;

    void Student2(String na, char s, int a, long n, int m, int e, int c){
        name = na;
        sex = s;
        age = a;
        number = n;
        math = m;
        english = e;
        computer = c;
    }
}

public class StudentExec {
    public static void main(String[] args) {

    }
}

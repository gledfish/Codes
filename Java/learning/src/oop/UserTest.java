package OOP;
/*
 * ClassName:UserTest
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 11:15
 * @author:gled fish
 */


/*
属性 和 局部变量
相同点：定义的格式相同：数据类型 变量名 = 变量值
       先声明，后使用
       都有对应的作用域
不同点：
        声明的位置不同
        属性：直接定义在类的一对{}中
        局部变量：声明在方法内，方法形参内，代码块内，构造器形参，构造器内部变量

        权限修饰符的不同
        属性：可以在声明属性时，使用权限修饰符指明其权限。、
        局部变量：不可以使用权限修饰符

        默认初始化值有区别
        属性：类的属性根据类型有对应的默认值
        局部变量：没有初始化值

        内存中加载的位置不同
        属性：加载到堆空间中
        局部变量：加载到栈空间


 */

class User{
    String name;
    int age;
    boolean isMale;

    public void talk(String language){
        System.out.println("我们说" + language);
    }

    public void eat(){
        String food = "烙饼";
        System.out.println("北方人喜欢吃：" + food);
    }
}
public class UserTest {
    public static void main(String[] args) {
        User u1 = new User();
        System.out.println(u1.name);
        System.out.println(u1.age);
        System.out.println(u1.isMale);
    }
}

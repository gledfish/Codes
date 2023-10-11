package OOP;

/*
 * ClassName:MethodArgsTest
 * Package:OOP
 * Project:learning
 * Description:
 * @Create:2023/2/2 - 9:39
 * @author:gled fish
 */

import java.util.Arrays;

class MethodArgs {
    public void show(int i){

    }
    public void show(String s){

    }
    public void show(String ... str){
        System.out.println(Arrays.toString(str));
    }
}


public class MethodArgsTest {
    public static void main(String[] args) {
        MethodArgs m1 = new MethodArgs();
        m1.show("hello");
        m1.show("hello", "world");
    }
}

package Array;/*
 * ClassName:ArrayException
 * Package:Array
 * Project:learning
 * Description:
 * @Create:2023/2/1 - 10:23
 * @author:gled fish
 */

public class ArrayException {
    public static void main(String[] args) {
        //        数组常见异常
//        1.数组角标异常
//        2.空指针异常
        int[] arr1 = new int[]{1, 2, 3};
        arr1 = null;
        System.out.println(arr1[0]);//空指针报错

        int[][] arr2 = new int[4][0];
        System.out.println(arr2[0]);//null
        System.out.println(arr2[0][0]);//空指针报错

    }
}

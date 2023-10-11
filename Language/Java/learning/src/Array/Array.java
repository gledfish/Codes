package Array;/*
 * ClassName:Main
 * Package:Array
 * Project:learning
 * Description:
 * @Create:2023/1/31 - 21:47
 * @author:gled fish
 */
import java.util.Arrays;

public class Array {

//    数组作为函数参数和函数返回值
    public static int[] reverse(int[] list){
        int[] result = new int[list.length];
        for(int i = 0, j = result.length - 1; i < list.length; i++,j--)
            result[j] = result[i];
        return result;
    }
    public static void main(String[] args) {
        int[] arr = new int[5]; //动态初始化
        String[] arr1 = new String[]{
                "Tom",
                "Jerry",
                "Jim"
        };//静态初始化
//        二维数组
        int[][] arr2 = new int[4][3];
        int[][] arr3 = new int[][]{
                {1,2,3},
                {4,5,6},
                {7,8,9}
        };


        //Arrays工具类的使用
//        1.判断数组是否相等
        int[] arr4 = new int[]{1,2,3,4};
        int[] arr5 = new int[]{1,2,3,4};
        boolean isEquals = Arrays.equals(arr4, arr5);
        System.out.println(isEquals);
//        2.数组生成字符串
        System.out.println(Arrays.toString(arr4));
//        3.数组填充
        int[] arr6 = new int[5];
        Arrays.fill(arr6,10);//全填充
        System.out.println(arr6[0]);
//        4.数组排序
        Arrays.sort(arr2);

//        5.二分查找
        int[] arr7 = new int[]{-98,-34,2,34,54,66,79,105,210,333};
        int index = Arrays.binarySearch(arr7, 34);
        System.out.println(index);

//
    }
}


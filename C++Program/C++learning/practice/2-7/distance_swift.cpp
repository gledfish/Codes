#include <iostream>
// 要求用户输入一个以long为单位的距离，然后将它转换为码


double* get_distance(int count);
    /* 获得用户的所有个数
    count:用户输入距离的个数
      返回一个距离数组*/
    
double* get_yard(double* distance_array, int count);
    /*对所有输入的距离进行转换
    distance:输入的距离数组
    count: 数组长度
    返回转换后的码距数组
    */

void show_result(double* result_array, int count);
    /*输出所有结果
    result_array:结果数组
    count:数组个数
    */
using namespace std;

int main(){
    int count = 2;
    double * distance_array = get_distance(count);
    double * result_array = get_yard(distance_array, count);
    show_result(result_array, count);

    return 0;
}

double* get_distance(int count){
    //
    double* distance_array = new double;
    for(int i = 0; i < count; i++){
        cout << "请输入距离：\n";
        cin >> distance_array[i];
    }
    return distance_array;
}

double* get_yard(double* distance_array, int count){
    /*对所有输入的距离进行转换
    distance:输入的距离数组
    返回转换后的码距数组
    */
   double* result_array = new double;
   int conver = 220;
   for(int i = 0; i < count; i++){
    result_array[i] = distance_array[i] * conver;
   }
   return result_array;
}

void show_result(double* result_array, int count){
    for(int i = 0; i < count; i++){
        // cout << result_array[i] << " ";
        printf("第%d个距离转换后的码距为%f\n", i+1, result_array[i]);
    }
    cout << endl;
}

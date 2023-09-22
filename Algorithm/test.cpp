#include <iostream>

using namespace std;

void showNum(int num){
    num++;
    cout << num <<endl;
}
int main(void) {
    int num = 0;
    cout << "请输入 num 的值"<< endl;
    cin >> num;
    cout << num << endl;
    showNum(num);
    return 0;
}
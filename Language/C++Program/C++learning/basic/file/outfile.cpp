#include <iostream>
#include <fstream> // 需要包含 fstream 头文件

using namespace std;
int main(){
    // 创建 fstream 对象
    fstream f("/home/gledfish/Codes/C++Program/C++learning/basic/file/outfile.txt", ios::in);

    //  打开文件
    if(!f.is_open()){
        cout << "文件打开失败" <<endl;
        perror("fopen");
        return 1;
    }

    //读取文件
    string line;
    while(getline(f,line)) {
        cout << line <<endl;
    }

    f.close();//关闭文件


    return 0;
}
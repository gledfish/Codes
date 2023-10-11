#include <vector>
#include <iostream>
using namespace std;
int main()
{
    vector<int> vi; // 创建一个整数数组

    int num;
    cout << "请输入数组的个数：\n";
    cin >> num;
    vector<double> vd(num);
    return 0;
    /*
    在C++中，`vector`类的一些常用方法包括：

- `push_back()`：在向量的末尾添加一个元素
- `pop_back()`：移除向量末尾的元素
- `size()`：返回向量中元素的数量
- `empty()`：检查向量是否为空
- `insert()`：在指定位置插入一个或多个元素
- `erase()`：删除一个元素或一系列元素
- `clear()`：移除所有元素
- `at()`：返回指定位置的元素
- `front()`：返回第一个元素
- `back()`：返回最后一个元素

*/
}
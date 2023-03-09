

// 输出快速排序递归算法隐含递归树的后序遍历序列
// 描述：
// 快速排序递归算法隐含一棵由关键字生成的二叉树（递归树），输出该隐含二叉树的后序遍历序列。（注：划分时以第一关键字为枢轴）
// 输入说明：
// 输入数据第一行为1个正整数n，表示关键字个数。第2行为n个整数表示n个关键字。
//     输出说明：
//         在一行上输出由关键字隐含的二叉树的后序遍历序列。
//             输入样例： 9 49 38 65 97 13 27 49 55 4 
// 输出样例： 27 13 38 4 49 55 65 97 49 提示
//                 在快速排序的过程中输出隐含二叉树的后序遍历序列，不用生成二叉树。

#include <stdio.h>
#include <iostream>
#include <vector>
#include <stdlib.h>

    using namespace std;
vector<int> a;
class Treenode
{
public:
    int val;
    Treenode *left;
    Treenode *right;
    Treenode(int x) : val(x), left(NULL), right(NULL) {}
};

int partition(vector<int> &a, int low, int high)
{
    int temp = a[low]; // 暂存枢值
    while (low != high)
    {
        while (low < high && a[high] >= temp)
            high--; // 找小于轴值的记录
        a[low] = a[high];
        while (low < high && a[low] <= temp)
            low++; // 找大于轴值的记录
        a[high] = a[low];
    }
    a[low] = temp;
    return low;
}

Treenode *Qssort(vector<int> &a, int low, int high)
{
    if (low > high)
        return NULL;
    int i = partition(a, low, high);
    Treenode *root = new Treenode(a[i]);
    root->left = Qssort(a, low, i - 1);
    root->right = Qssort(a, i + 1, high);
    return root;
}

void backordertrace(Treenode *root)
{
    if (root == NULL)
        return;
    backordertrace(root->left);
    backordertrace(root->right);
    cout << root->val << " ";
}

int main()
{
    int n = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int c;
        cin >> c;
        a.push_back(c);
    }
    Treenode *root;
    root = Qssort(a, 0, n - 1);
    backordertrace(root);
    system("pause");
    return 0;
}

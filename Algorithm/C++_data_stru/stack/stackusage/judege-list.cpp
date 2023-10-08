// 判断堆栈出栈序列是否有效
// 描述：
// 如果以序列“1, 2, 3, 4”作为一个栈（初始为空）的输入，那么可得到输出序列“1, 2, 3, 4”或“4, 3, 2, 1”或“2, 3, 1, 4”等等，但是肯定得不到输出序列“4, 1, 2, 3”或“3, 1, 2, 4”等等。请编写一个程序，判断能否通过一个栈得到给定的输出序列。 输入说明： 每组数据由两行构成，第一行只有一个整数n（ < 10），表示序列长度，同时表示栈的输入序列为“1, 2, 3,…, n”；第二行为n个整数，表示需要判断的出栈序列，整数之间以空格分隔。 输出说明： 输出一个yes或no（表示能否通过栈得到该序列）。 输入样例： 6 3 4 2 1 5 6 输出样例： yes 提示 根据栈的后进先出特性进行判断

#include <bits/stdc++.h>
#define MAX 10
    using namespace std;
// 定义栈
typedef struct Stack
{
    int items[MAX];
    int top; // 指向最高的元素
} myStack, *stackPoint;

// 创造空栈
stackPoint createEmpty(stackPoint sp)
{
    sp->top = -1;
    return sp;
}

// 判断栈空
bool isEmpty(stackPoint sp)
{
    int temp = sp->top;
    if (temp == -1)
        return true;
    else
        return false;
}

// 判断栈满
bool isFull(stackPoint sp)
{
    int temp = sp->top;
    if (temp == MAX - 1)
        return true;
    else
        return false;
}

// 往栈中添加一个元素
void pushElem(stackPoint sp, int num)
{
    if (!isFull(sp))
    {
        sp->top++;
        sp->items[sp->top] = num;
    }
}
// 从栈中删除一个元素
void pop(stackPoint sp)
{
    if (!isEmpty(sp))
    {
        sp -> top--;
    }
}
// 输出栈中所有元素
void stackPrint(stackPoint sp)
{
    if (!isEmpty(sp))
    {
        for (int i = 0; i <= sp->top; i++)
        {
            cout << sp->items[i] << endl;
        }
    }
}

int judgeList(stackPoint sp, int* nums, int length){
    int flag = 0;
    int i = 0;// 待检测序列的下标
    int j = 1;// 入栈出栈的元素
    pushElem(sp, j);//初始化第一个元素
    while(true){
        if(sp -> top == -1){
            //如果没有元素
            j++;
            pushElem(sp, j);
        }
        if(sp ->items[sp -> top] > nums[i]){// 栈顶元素不能大于待检测序列的元素，
            flag = 0;
            break;
        }
        if(sp ->items[sp -> top] < nums[i]){
            //继续添加元素
            j++;
            pushElem(sp, j);
        }
        if(sp ->items[sp ->top] == nums[i]){
            pop(sp);//出栈
            i++;//检测下一个元素
        }
        if (i == length){
            //检测完成
            flag = 1;
            break;
        }
    }
    return flag;
}
int main(void) {
    // 演示
    stackPoint sp = new myStack;
    createEmpty(sp);

    int length = 0;
    // printf("请输入长度：");
    scanf("%d", &length);

    // 输入待判断序列
    int nums[length];
    // printf("请输入待判断序列：");
    for(int i = 0; i < length; i++){
        scanf("%d", &nums[i]);
    }

    int flag = judgeList(sp, nums, length);
    if(flag){
        printf("yes");
    } else {
        printf("no");
    }
    delete sp;
    return 0;
}
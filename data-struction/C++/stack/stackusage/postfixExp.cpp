#include <bits/stdc++.h>
#define Max 10
using namespace std;
// 定义栈
typedef struct stack
{
    char items[Max];
    int top; // 指向最高的元素
} myStack;

// 创造空栈
myStack* createEmpty(myStack* sp)
{
    sp->top = -1;
    return sp;
}

// 判断栈空
bool isEmpty(myStack* sp)
{
    int temp = sp->top;
    if (temp == -1)
        return true;
    else
        return false;
}

// 判断栈满
bool isFull(myStack* sp)
{
    int temp = sp->top;
    if (temp == Max - 1)
        return true;
    else
        return false;
}

// 往栈中添加元素
bool push(myStack* sp, char elem)
{
    if (!isFull(sp))
    {
        sp->top++;
        sp->items[sp->top] = elem;
        return true;
    }
    return false;
}
// 输出栈中所有元素
void stackPrint(myStack* sp)
{
    if (!isEmpty(sp))
    {
        for (int i = 0; i <= sp->top; i++)
        {
            cout << sp->items[i];
        }
    }
}

int main(void)
{
    // demo
    myStack* sp = new myStack;
    sp = createEmpty(sp);
    int num = 7;
    printf("scanf:");
    // scanf("%c", );
    // push(sp, );
    cout << "success";
    stackPrint(sp);

    delete sp;
    return 0;
}


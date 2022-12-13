// 中心对称的字符串
// 描述：
// 对于有n个字符的字符串，设计算法判断字符串是否中心对称。例如，xyzzyx和xyzyx都是中心对称的字符串。
// 输入说明：
// 每组数据有2行：第一行为整数n，表示字符的个数，n小于100；第二行为n个字符组成的字符串。
// 输出说明：
// 判断这个字符串是否是中心对称的，是输出“YES”，不是输出“NO”。
// 输入样例：
// 12
// ThanksThanks
// 输出样例：
// NO

// #include <bits/stdc++.h>

// using namespace std;

// int main(void){
//     int count;
//     int flag = 1;
//     char centreString[100];
//     cin >> count;
//     for(int i = 0; i < count; i++){
//         cin >> centreString[i];
//     }
//     for(int i = 0; i < count / 2;i++){
//         if(centreString[i] != centreString[count-1-i]){
//             flag = 0;
//             break;
//         }
//     }
//     if (flag == 1){
//         cout << "YES";
//     } else
//         cout << "NO";
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

#define MAXSIZE 100
#define OK 1
#define ERROR 0
#define OVERFLOW -2
#define SElemType char
#define ElemType char
typedef int Status;
typedef struct
{
    SElemType *base;
    SElemType *top;
    int stacksize;
} SqStack;
typedef struct LNode
{
    ElemType data;
    static int max;
    struct LNode *next;
} LNode, *LinkList;
Status InitStack(SqStack &S)
{
    S.base = new SElemType[MAXSIZE];
    if (!S.base)
        exit(OVERFLOW);
    S.top = S.base;
    S.stacksize = MAXSIZE;
    return OK;
}
Status InitList(LinkList &L)
{
    LNode *p = L = new LNode;
    L->data = NULL;
    for (int i = 0;; i++)
    {
        LNode *s = new LNode();
        char a = cin.get();
        if (a == 10)
            break;
        s->data = a;
        s->max++;
        s->next = NULL;
        p->next = s;
        p = p->next;
    }
    return OK;
}
Status Push(SqStack &S, LinkList &L)
{
    int a = 0;
    LNode *t = L->next;
    for (int i = 0; i < L->max / 2; i++)
    {
        t = t->next;
    }
    if (L->max % 2 != 0)
    {
        t = t->next;
    }
    while (t)
    {
        *S.top++ = t->data;
        /**S.top = t->data;
        S.top++;*/
        t = t->next;
    }
    return OK;
}
bool Comparison(SqStack &S, LinkList &L)
{
    LNode *t = L->next;
    char e;
    while (S.top != S.base)
    {
        e = *--S.top;
        if (t->data != e)
        {
            return false;
        }
        t = t->next;
    }
    return true;
}
// int LNode::max = 0;
Status main()
{
    string str;
    SqStack s1;
    InitStack(s1);
    LinkList l;
    InitList(l);
    Push(s1, l);
    if (Comparison(s1, l))
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }
}
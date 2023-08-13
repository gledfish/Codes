// 数组顺序表
#include <bits/stdc++.h>
#define MaxSize 100

using namespace std;

typedef int Status;
typedef int ElemType;

typedef struct
{
    ElemType data[MaxSize];
    int length;
} SqList;

// 构造空的顺序表
SqList *initList(SqList *s)
{
    memset(s->data, 0, sizeof(s));
    s->length = 0;
    return s;
}

// 创建顺序表函数,初始化前n个数据、
SqList *CreateList(SqList *s, int n)
{
    if (n < 0 || n >= MaxSize)
    {
        cout << "初始化未成功" << endl;
        return s;
    }
    printf("输入数据：\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &s->data[i]);
        s->length++;
    }
    printf("输入完成：");
    return s;
}

// 插入函数：在位置i插入元素
SqList* InsertList(SqList *s, int i, ElemType e)
{
    if (i < 1 || i > s->length)
    {
        cout << "位置无效" << endl;
        return s;
    }
    if (s->length >= MaxSize)
    {
        cout << "存储空间已满" << endl;
        return s;
    }
    int num = i;
    for (int j= s->length; j >= i; j--)
    {
        s->data[j] = s->data[j - 1];
    }
    s->data[i - 1] = e;
    s->length++;
    return s;
}

// 查找函数，按位置查找元素e并返回其位置
int LocateElem(SqList *s, ElemType e)
{
    for (int i = 0; i < s->length; i++)
    {
        if (s->data[i] == e)
            return i + 1;
    }
    cout << "没找到" << endl;
    return 0;
}

// 倒置函数，将原顺序表倒置
SqList *ReverseList(SqList *s)
{
    if (s->length)
    {
        for (int i = 0; i < s->length - 1 - i; i++)
        {
            int temp = s->data[i];
            s->data[i] = s->data[s->length - 1 - i];
            s->data[s->length - 1 - i] = temp;
        }
    }
    return s;
}

// 奇偶分开并排序
//  清空顺序表
SqList *ClearList(SqList *s)
{
    s->length = 0;
    return s;
}

// 输出功能函数
void PrintSqList(SqList *s)
{
    cout << "当前顺序表所有元素：";
    for (int i = 0; i < s->length; i++)
    {
        cout << s->data[i] << "\t";
    }
    cout << "\n";
}

int main(void)
{
    SqList *s = new SqList;
    s = initList(s);
    int num = 5;
    s = CreateList(s, num);
    PrintSqList(s);
    s = InsertList(s, 1, 10);
    PrintSqList(s);
    delete s;
    return 0;
}
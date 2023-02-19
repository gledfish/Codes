// 输入一个整数组成的序列，
// 然后将序列中的奇数位置结点依序放在前面，偶数位置结点依序放在后面，组成一个新的序列。
// 输出此新序列。

#include <bits/stdc++.h>

typedef struct list
{
    int data;
    struct list *next;
} node, *List;
//Node

//创建新结点
void Create(List *p, int n)
{
    List tail, q;
    int i;
    *p = tail = (List)malloc(sizeof(node));
    (*p)->next = NULL;
    for (i = 0; i < n; i++)
    {
        q = (List)malloc(sizeof(node));
        scanf("%d", &q->data);
        q->next = NULL;
        tail->next = q;
        tail = q;
    }
    q->next = NULL;
}

void GetOdd(List p, int n)
{
    List q;
    int i;
    q = p->next;
    for (i = 0; i < n, q != NULL; i++)
    {
        if (i % 2 == 0)
        {
            printf("%d ", q->data);
        }
        q = q->next;
    }
}

void GetEven(List p, int n)
{
    List q;
    int i;
    q = p->next;
    for (i = 0; i < n, q != NULL; i++)
    {
        if (i % 2 != 0)
        {
            printf("%d ", q->data);
        }
        q = q->next;
    }
}

int main()
{
    List p;
    int n;
    scanf("%d", &n);
    Create(&p, n);
    GetOdd(p, n);
    GetEven(p, n);
    return 0;
}
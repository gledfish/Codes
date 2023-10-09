/*
指针链表

*/

#include <bits/stdc++.h>
// typedef int Status;
// typedef int ElemType;

using namespace std;

// 创建结点
typedef struct Node
{
    int val;
    Node *next;
} Node, *LinkedList;

// 创建空链表
LinkedList createEmptyLinkedList()
{
    LinkedList np = new Node;
    np->next = NULL;
    return np;
}

// 表头插入法创建表
LinkedList CreateLinkedList(LinkedList l, int num)
{
    int count = 0;
    cout << "请输入数据";
    while (count != num)
    {
        LinkedList p = new Node;
        if (!p)
        {
            cout << "创建失败";
            return l;
        }
        scanf("%d", &p->val);
        p->next = l->next;
        l->next = p;
        count++;
    }
    return l;
}
// 打印结点数据
void printLinklist(LinkedList l)
{
    LinkedList temp = new Node;
    temp = l;
    while (temp)
    {
        cout << temp->val << endl;
        temp = temp->next;
    }
}
//查找元素
LinkedList SearchElem(LinkedList l, int e){
    LinkedList temp = createEmptyLinkedList();
    temp = l;
    while(temp){
        if(temp ->val = e)
            return temp;
        temp = temp -> next;
    }
    cout <<"没找到元素e" <<endl;
    return l;
}
//在指定元素后插入元素
LinkedList InsertElem(LinkedList L, int i, int e){
    //要插入的节点
    LinkedList temp = createEmptyLinkedList();
    temp->val = e;
    // 之前的节点
    LinkedList p = createEmptyLinkedList();
    p = SearchElem(L, i);
    if(p ->val == i){
        p->next = temp;
    }
    temp -> next = L -> next;
    L -> next = p;
    return L;
}
//
int main(void)
{
    LinkedList l = createEmptyLinkedList();
    int num = 5;
    l = CreateLinkedList(l, num);
    printLinklist(l);
    return 0;
}

// 试题名称 3 - 1 链表去重 
// 问题描述： 给定一个键值为整数的单链表 L，将键值的绝对值有重复的结点删除：即对任意键值 K，只 有键值或其绝对值等于 K 的第一个结点被保留在 L 中。
// 例如，下面单链表 L 包含键值 21、 - 15、15、7、 - 15，；去重后的链表 L 包含键值 21、 - 15、7

/*
实现思路
    定义结点结构体，包括：地址，数据，写一个结点的位置，用5位整数表示
    输入结点个数，初始化结点数据
    定义整数数组，保存已出现的数据值。如果已经出现过则删除该结点，没出现过则将该结点的数据值加入数组
    输出剩余的链表
*/
#include <bits/stdc++.h>

using namespace std;

typedef struct Node
{
    int data;
    struct Node *next;
} Node, * LinkedList;

// 单链表初始化
LinkedList LinkedListInit()
{
    LinkedList l1 = new Node;
    l1->next = NULL;
    return l1;
}
// 建立单链表
//  bool buildLinkedList(LinkedList l){
//      int num;
//      scanf("%d",&num);
//      l -> data = num;
//      LinkedList l2 = new Node;
//      l -> next = l2;
//      l2 -> prev = l;
//      l2 -> next = NULL;
//      return true;
//  }

LinkedList LinkedListCreateH()
{
    Node* L = new Node;
    L->next = NULL;

    int x;
    cout << "请输入" << endl;
   //输入数据
    return L;
}

void printLinkedList(LinkedList l){
    LinkedList n = LinkedListInit();
    n = l;
    while (n)
    {
        /* code */
        cout << n ->data << endl;
        n = n -> next;
    }
    
}
int main(void)
{
    LinkedList l = LinkedListCreateH();
    printLinkedList(l);
    return 0;
}
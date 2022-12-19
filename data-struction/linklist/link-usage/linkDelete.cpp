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
// #include <algorithm>
#include <bits/stdc++.h>
using namespace std;

typedef struct Node {
    unsigned int Address;
    int data;
    unsigned int NextAddress;
    Node * next;
} Node, * Linklist;
int initNode(Linklist s,unsigned int Ads, int d, int Nds){
    Linklist p = new Node;
    p -> Address = Ads;
    p -> data = d;
    p -> NextAddress = Nds;
    s ->next = p;
    s = p;
    s -> next = NULL;
    delete p;
    return 0;
}
int initlist(int c, Linklist s){
    int Ads, d, Nds;
    for (int i = 0; i < c; i++){
    cin >> Ads >> d >> Nds;
    initNode(s, Ads, d, Nds);
    }
}

int isinArray(int * n, int num){
    for(int i = 0; i < 101; i++){
        if(n[i] == num){
            return 1;
        }
    }
    return 0;
}
int judgeData(Linklist s, int * n){
    int flag = isinArray(n, s -> data);
    if (flag == 0){
        // append();
    } else {
        // deleteNode();
    }
    return 0;
}
int main(void){
    int FAddress;
    int count;
    cin >> FAddress >> count;
    Linklist Linklist1 = new Node;
    initlist(count, Linklist1);

    int num[101];
    
    return 0;
}
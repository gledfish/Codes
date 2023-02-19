#include <bits/stdc++.h>

using namespace std;

//创建结点结构体
typedef struct Node
{
    int data;
    Node * next;
} Node, *NodePoint;

//打印结点数据
bool printLinklist(NodePoint np){
    while(np){
        cout << np -> data << endl;
        np = np -> next;
    }
    return true;
}
int main(void){
    NodePoint n1 = new Node;
    NodePoint n2 = new Node;
    NodePoint n3 = new Node;
    n1 -> data = 1;
    n1 -> next = n2;
    n2 -> data = 2;
    n2 -> next = n3;
    n3 -> data = 3;
    n3 -> next = NULL;
    printLinklist(n1);
    return 0;
}
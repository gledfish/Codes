#include <bits/stdc++.h>
#define MAX 5

using namespace std;
typedef struct circuQueue{
    int front;
    int rear;
    int data[MAX];
    int capacity;
}circuQueue, * queuePoint;

void createQueue(queuePoint qp){
    qp ->front = -1;
    qp -> rear = -1;
    qp ->capacity = 0;
}

bool isEmpty(queuePoint qp){
    if(qp ->front == -1)
        return true;
    else
        return false;
}
bool isFull(queuePoint qp){
    if(qp -> capacity == MAX)
        return true;
    else
        return false;
}


int main(void){
    return 0;
}
#include <bits/stdc++.h>
#define MAX 5

using namespace std;
typedef struct circuQueue{
    int front;
    int rear;
    int data[MAX];
}circuQueue, * queuePoint;

void createQueue(queuePoint qp){
    qp ->front = -1;
    qp -> rear = -1;
}

bool isEmpty(queuePoint qp){
    if(qp ->front == -1)
        return true;
    else
        return false;
}
bool isFull(queuePoint qp){
    if(qp -> front == 0 && qp -> rear == MAX - 1)
        return true;
    else if(qp ->front == qp -> rear + 1)
        return true;
    else
        return false;
}

bool enQueue(queuePoint qp, int num){
    if(!isFull(qp)){
        if(qp -> front == -1)
            qp -> front++;
        qp -> rear = (qp -> rear + 1) % MAX;
        qp -> data[qp -> rear] = num;
        return true;
        
    } else
        return false;

}

int deQueue(queuePoint qp)
{
    int element;
    if (isEmpty(qp))
    {
        cout << "Queue is empty" << endl;
        return (-1);
    }
    else
    {
        element = qp -> data[qp -> front];
        if (qp -> front == 0)
        {
            qp -> front = -1;
            qp -> rear = -1;
        }
        else
        {
            qp -> front = (qp -> front + 1) % MAX;
        }
        return element;
    }
}
void showQueue(queuePoint qp){
    if(!isEmpty(qp)){
        for(int i = qp -> front; i != qp -> rear + 1;i = (i + 1) % MAX){
        cout << qp -> data[i] << endl;
        }
    } else{
        cout << "empty";
    }
}


int main(void){
    queuePoint queuePoint = new circuQueue;
    createQueue(queuePoint);
    enQueue(queuePoint, 3);
    enQueue(queuePoint, 5);
    enQueue(queuePoint, 6);
    showQueue(queuePoint);
    return 0;
}
#include <bits/stdc++.h>
#define Max 10
#define ERROR 0
using namespace std;

typedef struct queue
{
    int front;
    int rear;
    int data[Max];
} myQueue, * queuePoint;

//初始化队列
void createQueue(queuePoint qp){
    qp -> front = -1;
    qp -> rear  = -1;
}
//判断队列空
bool isEmpty(queuePoint qp){
    if((qp -> front == -1) && qp -> rear == -1)
        return true;
    else 
        return false;
}
//判断队列满
bool isFull(queuePoint qp){
    if((qp->rear == Max -1) && (qp -> front == 0))
        return true;
    else
        return false;
}

// 将元素放入队列
bool enqueue(queuePoint qp, int num){
    if(!isFull(qp)){
        if(!isEmpty(qp)){
            qp->rear++;
            qp->data[qp->rear] = num;
            return true;
        } else{
            qp ->rear++;
            qp ->front++;
            qp ->data[qp->front] = num;
            return true;
        }
    } else 
            return false;
}
//从队列中取出元素
int dequeue(queuePoint qp){
    if(!isEmpty(qp)){
        if(qp->rear == 0){
            qp ->rear--;
            qp ->front--;
            return qp->data[qp->rear+1];
        } else{
            for(int i = 1;i <= qp->rear;i++)
            {
                qp->data[i-1] = qp->data[i];
            }
            qp->rear--;
            return qp->data[qp->data[qp->front]];
        }
    }else
        return ERROR;
}
//展示队列元素
void queuePrint(queuePoint qp){
    if(!isEmpty(qp)){
        for(int i = 0; i <= qp->rear; i++){
            cout << qp->data[i] << endl;
        }
    }
}

int main(void){
    queuePoint q1 = new myQueue;
    createQueue(q1);
    cout << isEmpty(q1) << endl;
    enqueue(q1, 34);
    enqueue(q1, 43);
    enqueue(q1, 45);
    queuePrint(q1);
    cout << isFull(q1) << endl;
    dequeue(q1);
    queuePrint(q1);
    return 0;
}
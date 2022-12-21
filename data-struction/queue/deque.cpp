#include <bits/stdc++.h>
#define Max 10
#define ERROR 0
using namespace std;

typedef struct deque
{
    int front;
    int rear;
    int data[Max];
} Deque, *dequePoint;

// 初始化队列
void createdeQue(dequePoint qp)
{
    qp->front = -1;
    qp->rear = -1;
}
// 判断队列空
bool isEmpty(dequePoint qp)
{
    if ((qp -> rear == -1) && (qp -> front == -1))
        return true;
    else
        return false;
}
// 判断队列满
bool isFull(dequePoint qp)
{
    if ((qp->rear == Max - 1) && (qp->front == 0))
        return true;
    else
        return false;
}

// 将元素从尾部放入队列
bool rearEnqueue(dequePoint qp, int num)
{
    if (!isFull(qp))
    {
        if (!isEmpty(qp))
        {
            qp->rear--;
            qp->data[qp->rear] = num;
            return true;
        }
        else
        {
            qp->rear = Max;
            qp->data[qp->rear] = num;
            return true;
        }
    }
    else
        return false;
}
// 从队列尾部中取出元素
int rearDequeue(dequePoint qp)
{
    if (!isEmpty(qp))
    {
        if (qp->rear == -1)
        {
            qp->front--;
            return qp->data[qp->front + 1];
        }
        else
        {
            qp->rear--;
            return qp->data[qp->rear+1];
        }
    }
    else
        return ERROR;
}

//从头部插入元素
bool frontEnqueue(dequePoint qp, int num)
{
    if (!isFull(qp))
    {
        if (!isEmpty(qp))
        {
            qp->front++;
            qp->data[qp->front] = num;
            return true;
        }
        else
        {
            qp->front = 0;
            qp->data[qp->front] = num;
            return true;
        }
    }
    else
        return false;
}
// 从队列头部中取出元素
int frontDequeue(dequePoint qp)
{
    if (!isEmpty(qp))
    {
        if (qp->front == -1)
        {
            qp->rear--;
            return qp->data[qp->rear + 1];
        }
        else
        {
            qp->front--;
            return qp->data[qp->front + 1];
        }
    }
    else
        return ERROR;
}
// 展示队列元素
void queuePrint(dequePoint qp)
{
    if (!isEmpty(qp))
    {
        for (int i = qp->rear; i !=  qp->front + 1; i = (i+1)%Max)
        {
            cout << qp->data[i] << endl;
        }
    }
}

int main(void)
{
    dequePoint q1 = new Deque;
    createdeQue(q1);
    rearEnqueue(q1, 34);
    rearEnqueue(q1, 43);
    rearEnqueue(q1, 45);
    queuePrint(q1);
    rearDequeue(q1);
    queuePrint(q1);
    return 0;
}
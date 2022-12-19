package queue;

class SimpleQueue {
    int front;
    int rear;
    int data[];
    int capacity;

    //构造一个给定容量的队列
    SimpleQueue(int size){
        front = -1;
        rear  = -1;
        data = new int[size];
        capacity = size;
    }

    public Boolean isEmpty(){
    if (front == -1)
        return true;
    else 
        return false;
}

    public Boolean isFull(){
    if((rear == capacity -1) && (front == 0))
        return true;
    else
        return false;
}

    public Boolean enqueue(int num){
    if(!isFull()){
        if(!isEmpty()){
            rear++;
            data[rear] = num;
            return true;
        } else{
            rear++;
            front++;
            data[front] = num;
            return true;
        }
    } else 
            return false;
}
//从队列中取出元素
    public int dequeue(){
    if(!isEmpty()){
        if(rear == 0){
            rear--;
            front--;
            return data[rear+1];
        } else{
            for(int i = 1;i <= rear;i++)
            {
                data[i-1] = data[i];
            }
            rear--;
            return data[front];
        }
    } else{
        System.out.println("empty");
        return 0;
    }
}
//展示队列元素
    public void queuePrint(){
    if(!isEmpty()){
        for(int i = 0; i <= rear; i++){
            System.out.println(data[i]);
        }
    }
}
    public static void main(String[] args) {
        SimpleQueue queue = new SimpleQueue(5);
        queue.enqueue(5);
        queue.enqueue(9);
        queue.queuePrint();
        queue.dequeue();
        queue.queuePrint();
    }
}

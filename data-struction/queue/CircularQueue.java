package queue;

public class CircularQueue {
    private int front;
    private int rear;
    private int data[];
    private int size;

    CircularQueue(int s){
        front = -1;
        rear = -1;
        size =  s;
        data = new int[s];
    }

    public Boolean isEmpty(){
        if (front == -1)
            return true;
        else 
            return false;
    }

    public Boolean isFull(){
        if (front == 0 && rear == size - 1)
            return true;
        else if (front == rear + 1)
            return true;
        else
            return false;
    }

    Boolean enQueue(int num){
    if(!isFull()){
        if(front == -1)
            front++;
        rear = (rear + 1) % size;
        data[rear] = num;
        return true;
    } else
        return false;
}
    public int deQueue() {
    int element;
    if (isEmpty()) {
        System.out.println("Queue is empty");
        return (-1);
    } else {
        element = data[front];
        if (front == 0)
        {
            front = -1;
            rear = -1;
        }
        else
            front = (front + 1) % size;
        return element;
    }
}

    public void showQueue(){
    if(!isEmpty()){
        for(int i = front; i != rear + 1;i = (i + 1) % size){
            System.out.println(data[i]);
        }
    } else
        System.out.println("empty");
}

    public static void main(String[] args) {
        CircularQueue q1 = new CircularQueue(5);
        q1.enQueue(3);
        q1.enQueue(4);
        q1.enQueue(4);
        q1.showQueue();
        q1.deQueue();
        q1.showQueue();
    }
}

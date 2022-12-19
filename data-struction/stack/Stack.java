package stack;

class Stack{
    private int arr[];
    private int top;
    private int capacity;

    //使用构造方法构造一个栈
    Stack(int size){
        arr = new int[size];
        capacity = size;
        top = -1;
    }

    //栈类的方法
    //入栈
    public void push(int x){
        if(isFull()) {
            System.out.println("full");
            System.exit(1);
        }
        arr[++top] = x;
    }

    //判断栈满
    public Boolean isFull(){
        return top == capacity - 1;
    }

    //判断栈空
    public Boolean isEmpty(){
        return top == -1;
    }

    //出栈
    public int pop(){
        if(isEmpty()){
            System.out.println("empty");
            System.exit(1);
        }
        return arr[top--];
    }


    //获得栈当前元素的数量
    public int size(){
        return top + 1;
    }

    //获得栈当前所有元素
    public void printStack(){
        for (int i = 0; i <= top;i++){
            System.out.println(arr[i]);
        }
    }


public static void main(String[] args) {
    Stack stack = new Stack(5);
    stack.push(1);
    stack.printStack();
    stack.pop();
    stack.printStack();
}

}

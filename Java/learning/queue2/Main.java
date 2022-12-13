package learning.queue2;

public class Main {
    public static void main(String[] args) {
        Queue q1 = new Queue(10);

        char[] name = {'T', 'O', 'M'};
        Queue q2 = new Queue(name);
        for(int i = 0; i < 10; i++)
            q1.put((char)('A'+i));
        Queue q3 = new Queue(q1);
        //输出队列
        for(int i = 0; i < 10; i++){
            System.out.print(q1.get());
            System.out.print(" ");
        }
        System.out.println();
        for (int i = 0; i < 3; i++) {
            System.out.print(q2.get());
            System.out.print(" ");
        }
        System.out.println();
        for (int i = 0; i < 10; i++) {
            System.out.print(q3.get());
            System.out.print(" ");
        }
        System.out.println();
    }
}

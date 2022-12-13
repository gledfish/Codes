package learning.queue;

public class Queue {
    char[] q;
    int putloc, getloc;

    Queue(int size){
        q = new char[size];
        putloc = getloc = 0;
    }
    void put(char ch){
        if (putloc == q.length){
            System.out.print("FULL");
            return;
        }
        q[putloc++] = ch;
    }

    char get(){
        if (getloc == putloc){
            System.out.println("EMPTY!");
            return (char)0;
        }
        return q[getloc++];
    }
}

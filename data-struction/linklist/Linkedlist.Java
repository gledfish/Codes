
public class Linkedlist{
    //结点类
    static class Node {
        int value;
        Node next;

        //结点构造方法
        Node(int d){
            value = d;
            next = null;
        }
    }

    Node head;
    public static void main(String[] args) {
        Linkedlist linkedlist = new Linkedlist();

        linkedList.head = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);

        linkedList.head.next = second;
        second.next = third;

         // printing node-value
        while (linkedList.head != null) {
        System.out.println(linkedList.head.value);
        linkedList.head = linkedList.head.next;
        }
    }
}
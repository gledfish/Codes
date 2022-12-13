package learning.queue;

public class Main {
    public static void main(String[] args) {
        Queue bigQ = new Queue(100);
        char ch;
        for (int i = 0; i < 26; i++){
            bigQ.put((char)('A' + i));
        }
        for (int i = 0; i < 26; i++){
            ch = bigQ.get();
            if(ch != (char) 0)
                System.out.println(ch);
        }
        System.out.println("\n");
    }
}

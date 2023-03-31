package Exercise;

/*
 * ClassName:TestThread
 * Package:Exercise
 * Project:learning
 * Description:
 * @Create:2023/3/31 - 16:43
 * @author:gled fish
 */
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class TestThread implements Runnable{
    @Override
    public void run() {
        // 重写 run 方法，方便测试
        System.out.println("执行线程!");
    }
    public static void main(String[] args) throws Exception {
        ExecutorService e=Executors.newFixedThreadPool(4);
        for (int i = 0; i < 4; i++) {
            Thread t=new Thread(new TestThread());
            //执行线程体
			t.start();
        }
        e.shutdown();
    }
}
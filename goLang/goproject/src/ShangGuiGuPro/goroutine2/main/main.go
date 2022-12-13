package main
import (
	"fmt"
	"sync"
)
var wg sync.WaitGroup

func main() {
	wg.Add(1)//计数牌加1
	go hello()//开启一个独立的goroutine来执行hello函数
	fmt.Println("hello, main")
	//等待程序执行完毕方式一
	//time.Sleep(time.Second)不推荐
	//方式2：
	wg.Wait()//等所有线程结束时程序结束

go func() {
	fmt.Println("hello")
}
}

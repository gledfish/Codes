package main

import (
	"fmt"
    "sync"
	"strconv"
	//"time"
	"runtime"
)
var wg sync.WaitGroup

func hello() {
	for i := 0; i < 10; i++ {
		fmt.Println("hello, world" + strconv.Itoa(i))
	    wg.Done()//通知wg计数器-1
	}
}

func main() {
	wg.Add(10)//计数牌加1
	go hello()//开启一个独立的goroutine来执行hello函数
	for i := 0; i < 10; i++ {
		fmt.Println("hello, main~world" + strconv.Itoa(i))
	}
	//等待程序执行完毕方式一
	//time.Sleep(time.Second)不推荐
	//方式2：
	wg.Wait()//等所有线程结束时程序结束
	fmt.Println(runtime.NumCPU())
}

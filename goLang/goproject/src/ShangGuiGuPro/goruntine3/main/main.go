package main
import (
	"runtime"
	"fmt"
	//"time"
	"sync"
)

var wg sync.WaitGroup

var (
	myMap = make(map[uint]uint,10)
	//lock是一个全局的互斥锁
	lock sync.Mutex
)

//计算n的阶乘，放入Map中
func test(n uint) {
	var res uint
	res = 1
	var i uint
	for i = 1; i <= n; i++ {
		res *= i
	}
	lock.Lock()
	myMap[n] = res
	lock.Unlock()
	wg.Done()
}
func main() {
	wg.Add(20)

	//可以自己设置使用多个cpu
	runtime.GOMAXPROCS(16)

	//起协程
	for i := 1; i <= 20; i++ {
		go test(uint(i))
	}

	wg.Wait()
	//休眠多少呢？
	//time.Sleep(time.Second * 10)
	//输出结果
	for i, v := range myMap {
		fmt.Printf("map[%v] = %v\n", i, v)
	}
}
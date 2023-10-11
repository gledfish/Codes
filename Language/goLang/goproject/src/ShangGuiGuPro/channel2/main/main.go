package main
import (
	"fmt"
)

func main() {
	//创建一个可以存放3个int类型的管道
	var intChan chan int
	intChan = make(chan int, 3)

	//看看intChan是什么？
	// fmt.Printf("intChan的值=%v\nintChan的地址为%v\n", intChan, &intChan)
	intChan <- 10
	num := 211
	intChan <- num
	intChan <- num
	//4.看看管道的长度和容量
	//容量不会自动增加
	fmt.Println(len(intChan), cap(intChan))

	//从管道中读取数据
	var num2 int
	num2 = <- intChan
	fmt.Println(num2)
	//在没有使用协程的情况下，如果我们的管道数据已经全部取出，再取就会报告
	fmt.Println(len(intChan), cap(intChan))
	
}
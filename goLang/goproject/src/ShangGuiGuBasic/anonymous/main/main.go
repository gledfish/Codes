package main

import "fmt"

var ( fun1 = func (n1 int, n2 int) int {
		return n1 * n2
	}
)
func main() {
	//第一种方式
	res1 := func (n1 int, n2 int) int {
		return n1 + n2
	}(10,20)
	fmt.Println(res1)
	//第二种方法
	a := func (n1 int, n2 int) int {
		return n1 - n2
	}
	res2 := a(10, 30)
	fmt.Println(res2)
	//第三种用法：全局匿名函数
	res4 := fun1(4,9)
	fmt.Println(res4)
}
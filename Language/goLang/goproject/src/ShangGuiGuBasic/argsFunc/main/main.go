package main

import "fmt"

func sum(n1 int, args ...int) int {
	sum := n1
	for index, _ := range args {
		sum += args[index] //取出args中第一个元素的值
	}
	return sum
}
func main() {
	res4 := sum(10, 0, 10, 10, 10)
	fmt.Println(res4)
}

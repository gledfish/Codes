package main

import (
	"fmt"
)

func AddUpper() func (int) int {
	var n int = 10
	var str = "hello"
	return func (x int) int {
		n = n + x
		str += "a"
		fmt.Println("str =", str)
		return n
	}
}

func main() {
	//使用AddUpper
	f := AddUpper()
	fmt.Println(f(1))
	fmt.Println(f(2))
	fmt.Println(f(3))
}
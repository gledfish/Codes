package main

import (
	"fmt"
)
//一个被测试的函数
func addUpper(n int) int {
	res := 0
	for i := 1; i <= n; i++ {
		res += i
	}
	return res
}

func main() {
	res := addUpper(10)
	fmt.Println(res)
}
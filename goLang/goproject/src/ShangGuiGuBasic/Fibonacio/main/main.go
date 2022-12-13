package main

import "fmt"

func fibonacci(num int) (slice []uint64) {
	slice = make([]uint64, num)
	slice[0] = 1
	slice[1] = 1
	for i := 2; i < num; i++ {
		slice[i] = slice[i-1] + slice[i-2]
	}
	return slice
}
func main() {
	var num int
	fmt.Println("请输入斐波那契数列的项数：")
	fmt.Scanln(&num)
	slice := fibonacci(num)
	fmt.Println(slice)
}

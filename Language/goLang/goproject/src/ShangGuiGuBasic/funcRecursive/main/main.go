package main

import "fmt"

func funcRecursive(num int) int {
	if num == 1 {
		return 3
	} else {
		result := 2 * funcRecursive(num - 1) + 1 
		return result
}
}
func main() {
	var num int
	fmt.Println("请输入一个数字：")
	fmt.Scanln(&num)
	result := funcRecursive(num)
	fmt.Println(result)
}
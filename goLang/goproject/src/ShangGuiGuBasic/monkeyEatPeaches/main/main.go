package main

import "fmt"

func peachNum(num int) int {
	if n > 10 || n < 1 {
		fmt.Println("输入的天数不对")
		return 0
	}
	if num == 10 {
		return 1
	} else {
		result := (peachNum(num + 1) + 1 ) * 2
		return result
}
}
func main() {
	var num int
	fmt.Println("请输入天数：")
	fmt.Scanln(&num)
	result := peachNum(num)
	fmt.Println(result)
}
package main

import (
	"fmt"
	"strconv"
)
func main() {
	// //len()
	// str := "hello北"
	// fmt.Println("str len =", len(str))
	//
//字符串遍历，同时处理有中文的问题
	// str2 := "hello北京"
	// str := []rune(str2)
	// for i := 0; i < len(str); i++ {
	// 	fmt.Printf("%c\n", str[i])
	// }
	//字符串转整数：n, err := strconv.Atoi("12")
	n, err := strconv.Atoi("123")
	if err != nil {
		fmt.Println("转换错误", err)
	} else {
		fmt.Println("转换的结果为：", n)
	}
	
}
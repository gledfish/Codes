package main

import (
	"fmt"
)

func main() {
	// var intArr[3]int
	// fmt.Println(intArr)
	// fmt.Printf("%p %p %p", &intArr, &intArr[0], &intArr[1])
	// var floatArr[5] float64
	// for i := 0; i < len(floatArr); i++ {
	// 	fmt.Printf("请输入第%d个成绩： ", i+1)
	// 	fmt.Scanln(&floatArr[i])
	// }
	// fmt.Println(floatArr)
	intArr := [3]int {1, 2, 3}
	fmt.Println(intArr)
	fmt.Printf("%p %p %p", &intArr, &intArr[0], &intArr[1])
}
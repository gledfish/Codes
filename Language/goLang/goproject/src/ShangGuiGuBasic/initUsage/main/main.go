package main

import (
	"fmt"
	"initUsage/utils"
)
var age = test()
func test() int {
	fmt.Println("test()")
	return 90
}
//init函数
func init() {
	fmt.Println("init()...")
}

func main() {
	fmt.Println("main()...")
	fmt.Println("Age = ", utils.Age, "Name =", utils.Name)
}
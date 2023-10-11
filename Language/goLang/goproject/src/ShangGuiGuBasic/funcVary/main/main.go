package main

import (
	"fmt"
)

func getSum(n1 int, n2 int) int {
	return n1 + n2
}

func myFun(funvar func(int, int) int, num1 int, num2 int) int {
	return funvar(num1, num2)
}
func main() {
	a := getSum
	fmt.Printf("a的类型是%T,getSum类型是%T\n", a, getSum)
	res := a(10, 40)
	fmt.Println("res=", res)

	res2 := myFun(getSum, 50, 60)
	fmt.Println("res2 =", res2)
}
package main

import (
	"fmt"
)

func main() {
	// var intArr [5] int = [...]int {1, 22, 33, 66, 99}
	// slice := intArr[:]//左闭右开
	// fmt.Println("intArr= ", intArr)
	// fmt.Println("slice 的元素 =", slice)
	// fmt.Println("slice的元素个数 =", len(slice))
	// fmt.Println("slice 的容量 =", cap(slice))//切片的容量可以动态变化
	// slice[1] = 34
	// fmt.Println("intArr= ", intArr)
	// fmt.Println("slice 的元素 =", slice)
	// fmt.Println("slice的元素个数 =", len(slice))
	// fmt.Println("slice 的容量 =", cap(slice))//切片的容量可以动态变化
	var slice1 []int = make([]int, 4, 8)
	fmt.Println(slice1)
	slice2 := make([]int, 5)
	fmt.Println(slice2)
}
package main

import "fmt"

func main() {
	//二维数组的使用
	// var arr2[2][2]int
	// arr2[1][1] = 10
	// fmt.Println(arr2)
	// fmt.Printf("%p\n", &arr2[0])
	// fmt.Printf("%p\n", &arr2[1][0])
	// arr3 := [2][3]int{{1, 2, 3}, {4, 5, 6}}
	// fmt.Println(arr3)

	//二维数组的遍历
	array := [2][3]int {{1, 2, 3},{4, 5, 6}}
	for i := 0; i < len(array); i++ {
		for j := 0; j < len(array[i]); j++ {
			fmt.Print(array[i][j], " ")
		}
		fmt.Println()
	}
	for index1, value1 := range array {
		for index2, value2 := range value1 {
			fmt.Printf("array[%d][%d] = %d\n", index1, index2, value2)
		}
	}
}

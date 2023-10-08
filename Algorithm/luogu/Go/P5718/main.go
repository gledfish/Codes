package main

import (
	"fmt"
)

func main() {
	arrayNum := 0
	fmt.Scan(&arrayNum)
	var array [100]int
	for i := 0; i < arrayNum; i++ {
		fmt.Scan(&array[i])
	}
	for i := 0; i < arrayNum - 1; i++ {
		for j := 0; j < arrayNum - 1 - i; j++ {
			if array[j] > array[j+1] {
				temp := 0
				temp = array[j+1]
				array[j+1] = array[j]
				array[j] = temp
			}
		}
	}
	fmt.Println(array[0])
}
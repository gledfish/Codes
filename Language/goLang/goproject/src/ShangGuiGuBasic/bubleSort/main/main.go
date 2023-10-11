//这是一个冒泡排序
package main

import "fmt"

func BinaryFind(array *[]int, num int) {
	for i := 0; i < len(*array)-1; i++ {
		for j := 0; j < len(*array)-i-1; j++ {
			if (*array)[j] > (*array)[j+1] {
				temp := (*array)[j]
				(*array)[j] = (*array)[j+1]
				(*array)[j+1] = temp
			}
		}
	}
	var leftIndex int
	rightIndex := len(*array) - 1
	midIndex := rightIndex / 2
	for {
		if num < (*array)[midIndex] {
			rightIndex = midIndex
			midIndex = (leftIndex + rightIndex) / 2
		} else if num > (*array)[midIndex] {
			leftIndex = midIndex
			midIndex = (leftIndex + rightIndex) / 2
		} else if num == (*array)[midIndex] {
			fmt.Println("已经找到，下标为", midIndex)
			break
		} else if leftIndex >= rightIndex {
			break
		}
	}
}
func main() {
	slice := []int{2, 4, 3, 5, 1, 8, 5}
	slice = append(slice, 78, 8, 9, 16, 78, 89, 56)
	var num int
	fmt.Println("请输入一个数字")
	fmt.Scanln(&num)
	BinaryFind(&slice, num)
}

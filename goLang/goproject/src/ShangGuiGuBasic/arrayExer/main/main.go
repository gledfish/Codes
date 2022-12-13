package main

import (
  "fmt"
  "math/rand"
  "time"
)

func main() {
// 	题目1：输出字母表
// 	byteArray := [26]byte{}
// 	for index, _ := range byteArray {
// 		byteArray[index] = 'A' + byte(index)
// 	}
// 	fmt.Println("即将输出字母表，做好准备！")
// 	for i := 0; i < len(byteArray); i++ {
// 		fmt.Printf("%c\n", byteArray[i])
// 	}
// 	题目2：数组的最大值
// 	nums := [4]int{4, 8, 9, 6}
// 	max := 0
// 	maxIndex := 0
// 	for index, _ := range nums {
// 		if nums[index] > max {
// 			max = nums[index]
// 			maxIndex = index
// 		}
// 	}
// 	fmt.Println("数组的最大值为：", max, "最大值的下标为：", maxIndex)
// 	题目3：数组的和及平均值
// 	nums := [5]int{4, 8, 9, 6, 4}
// 	sum := 0
// 	for index, _ := range nums {
// 		sum += nums[index]
// }
//     fmt.Println("数组的和为：", sum, "数组的平均值为：", float64(sum) / float64(len(nums)))
  intArr := [5]int {}
  rand.Seed(time.Now().UnixNano())
  for i := 0; i < len(intArr); i++ {
  	intArr[i] = rand.Intn(100)
  }
  fmt.Println(intArr)
  for i := 0; i < len(intArr) / 2; i++ {
  	temp := intArr[i]
  	intArr[i] = intArr[len(intArr)-1-i]
  	intArr[len(intArr)-1-i] = temp 
  }
  fmt.Println(intArr)
}
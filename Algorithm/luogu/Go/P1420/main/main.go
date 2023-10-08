package main

import (
	"fmt"
)

func main() {
	var judgeNum int
	result := 1
	length := 1
	fmt.Scan(&judgeNum)
	scores := [10000]int64{}
	for i := 0; i < judgeNum; i++ {
		fmt.Scan(&scores[i])
	}
	for i := 1; i < judgeNum; i++ {
		if scores[i] == (scores[i-1] + 1) {
		   length++
		} else if length > result {
			result = length
			length = 1
		} else {
			length = 1
		}
	}
	fmt.Println(result)
}
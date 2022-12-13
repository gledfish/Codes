package main

import (
	"fmt"
	"sort"
)

func main() {
	judgeNum := 0
	fmt.Scan(&judgeNum)
	scores := [1000]int{}
	for i := 0; i < judgeNum; i++ {
		fmt.Scan(&scores[i])
	}
	var scoreSlice = scores[:judgeNum]
	sort.Ints(scoreSlice)
	result := scoreSlice[judgeNum - 1] - scoreSlice[0]
	fmt.Println(result)
}
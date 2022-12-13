package main

import (
	"fmt"
	"sort"
)

func main() {
	judgeNum := 0
	sum := 0
	fmt.Scan(&judgeNum)
	scores := [1000]int{}
	for i := 0; i < judgeNum; i++ {
		fmt.Scan(&scores[i])
	}
	var scoreslice = scores[:judgeNum]
	sort.Ints(scoreslice)
	scoreslice2 := scoreslice[1:judgeNum-1]
	for _, v := range scoreslice2 {
		sum += v
	}
	var average float64 = float64(sum) / float64(judgeNum - 2)
	fmt.Printf("%.2f", average)
}
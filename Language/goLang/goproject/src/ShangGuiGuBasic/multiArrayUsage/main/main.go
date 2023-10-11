package main

import "fmt"

func main() {
	sum := 0
	sumArray := [3]int {}
	scores := [3][5] int {{60, 80, 60, 60, 60}, {80, 80, 80, 60, 70}, {100, 100, 80, 70, 100}}
    for i := 0; i < len(scores); i++ {
    	for j := 0; j < len(scores[i]); j++ {
    		sumArray[i] += scores[i][j]
    		sum += scores[i][j]
    	}
    }
    averageSum := float64(sum) / float64(len(scores) * len(scores[0]))
    fmt.Printf("所有班的平均成绩是：%.2f\n", float64(averageSum))
    for i, v := range sumArray {
    	fmt.Printf("第%d个班的平均成绩是：%.2f\n", i+1, float64(v) / float64(len(scores[0])))
    }
}
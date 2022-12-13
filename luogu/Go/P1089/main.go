package main

import (
	"fmt"
)

func main() {
	const monthNum = 12
	money := 0; remain := 0
	var spentMoney [monthNum] int
	for i := 0; i < monthNum; i++ {
		fmt.Scan(&spentMoney[i])
		if (remain + 300 - spentMoney[i] < 0){
			fmt.Println(-i - 1)
			break
		}
		money += (remain + 300 - spentMoney[i]) / 100
		remain = (remain + 300 - spentMoney[i]) % 100
		if i == 11 {
			fmt.Println(money * 120 + remain)
		}
	}
}
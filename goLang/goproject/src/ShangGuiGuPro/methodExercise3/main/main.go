package main

import "fmt"

type Mutiply struct {
	Num1 int
	Num2 int
}

func (mutiply *Mutiply) print() {
	for i := 1; i <= mutiply.Num1; i++ {
		for j := 1; j <= i; j++ {
			fmt.Printf(" %d * %d = %d", j, i, i*j)
		}
		fmt.Println()
	}
}
func main() {
	var mutiplyNum Mutiply = Mutiply{9, 9}
	mutiplyNum.print()
}

package main

import "fmt"

func getSumAndSub(n1 int, n2 int) (int, int) {
	sum := n1 + n2
	sub := n1 - n2
	return sum, sub
}

func main() {
	ret1, ret2 := getSumAndSub(1, 2)
	fmt.Printf("ret1 = %#v ret2 = %#v\n", ret1, ret2)
}
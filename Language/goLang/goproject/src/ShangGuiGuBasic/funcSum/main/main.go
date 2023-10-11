package main

import "fmt"

func getSum(n1 int, n2 int) int {
	sum := n1 + n2
	return sum
}

func main() {
	sum := getSum(10, 20)
	fmt.Println("main sum = ", sum)
}
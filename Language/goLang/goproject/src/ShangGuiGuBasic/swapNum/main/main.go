package main

import "fmt"

func swap(n1 *int, n2 *int)  {
	var temp int
	temp = *n1
	*n1 = *n2
	*n2 = temp
}
func main() {
	n1 := 1
	n2 := 2
	swap(&n1, &n2) 
	fmt.Println(n1, n2)
}
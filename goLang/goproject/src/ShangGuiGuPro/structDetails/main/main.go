package main

import "fmt"

type Point struct {
	x int
	y int64
}

type Rect struct {
	leftUp, rightDown Point
}
func main() {
	r1 := Rect{Point{1, 2},Point{3,4}}
	fmt.Printf("%p\n", &(r1.leftUp.x))
	fmt.Printf("%p\n", &(r1.leftUp.y))
	fmt.Printf("%p\n", &(r1.rightDown.x))
	fmt.Printf("%p\n", &(r1.rightDown.y))
}
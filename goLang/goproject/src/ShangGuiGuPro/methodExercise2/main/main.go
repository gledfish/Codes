package main

import "fmt"
type Matrix struct {
	matrix1 [3][3] int
}

func (matrix *Matrix) reverse () {
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			fmt.Printf("%d ", matrix.matrix1[j][i])
		}
		fmt.Println()
	}
}
func main() {
	var matrix Matrix = Matrix {
		[3][3] int {
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9},
		},
	}
	matrix.reverse()
}
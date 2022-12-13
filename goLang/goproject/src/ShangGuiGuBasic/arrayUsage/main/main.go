package main

import "fmt"

func main() {
	var hens[4] float64;
	hens[0] = 1.0
	hens[1] = 2.0
	hens[2] = 3.0
	hens[3] = 4.0
	var total float64 = 0.0
	for i := 0; i < len(hens); i++ {
		total += hens[i]
	}
	avgWeight := fmt.Sprintf("%.2f", total / float64(len(hens)))
	fmt.Println(avgWeight)
}
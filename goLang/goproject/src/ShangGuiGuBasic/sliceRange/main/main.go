package main
import (
	"fmt"
)

func main() {
	slice := []int {10, 20, 30, 40, 50, 60}
	for index, value := range slice {
		fmt.Printf("slice[%v] = %v\n", index, value)
	}
	//append的使用
	fmt.Println(slice)
	slice2 := append(slice, 70, 80)
	slice = append(slice, slice2...)
	fmt.Println(slice)
	slice3 := make([]int, 10)
	copy(slice3, slice)
	fmt.Println(slice3)
}

package main

import (
	"fmt"
)

func test(pointer *[3]int) {
	(*pointer)[0] = 88
	fmt.Println(pointer)
}

func main() {
	// heroes := [3] string {"宋江", "吴用", "黑旋风"} 
	// for _, value := range heroes {
	// 	fmt.Printf("value = %#v\n", value)
	// }
	// boolArray := [3] bool{false, true, true}
	// fmt.Println(boolArray)
	arr := [3] int {11,22,33}
	fmt.Println(&arr)
	test(&arr)
	fmt.Println(arr)
}
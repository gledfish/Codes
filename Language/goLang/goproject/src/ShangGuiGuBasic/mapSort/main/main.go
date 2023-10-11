package main

import (
	"fmt"
	"sort"
)
func main() {
	map1 := make(map[int]int)
	map1[10] = 100
	map1[1]  = 13
	map1[4]  = 56
	map1[5]  = 57
	fmt.Println(map1)
	//golang中是先排序map中的key放入切片中
	//先对切片排序
	//遍历切片，然后按照key来输出map的值

	var keys []int
	keys = make([]int, 2)
	for i, _ := range map1 {
		keys = append(keys, i)
	}
	sort.Ints(keys)
	fmt.Println(keys)
}
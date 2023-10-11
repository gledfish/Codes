package main

import "fmt"

type Person struct {
	Name string
	Address string
	Age int
	Sex int
	Income int
	Scores [5]float64
	ptr *int//指针
	slice []int//切片
	map1 map[string]string//map
}

func main () {
	var p1 Person
	p1.Age = 10
	p1.Name = "小明"
	//var p2 *Person = &p1

	// fmt.Println(p2.Age)
	// p2.Name = "tom"
	// fmt.Println(p2.Name, p1.Name)
	// fmt.Printf("%p\n", &p1)
	// // fmt.Println(p2)
	// fmt.Printf("%p, %p", &p2, p2)

	fmt.Printf("%p\n", &(p1.Name))
	fmt.Printf("%p\n", &(p1.Address))
	fmt.Printf("%p\n", &(p1.Age))
	fmt.Printf("%p\n", &(p1.Sex))
	fmt.Printf("%p\n", &(p1.Income))
}
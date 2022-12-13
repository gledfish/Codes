package main

import "fmt"

//定义一个cat结构体
type Cat struct {
	Name string
	Age int
	Color string
	Hobby string
	StringPoint *string
}

type Heroes struct {
	Name string
	HeroSex string
	talents [4]string
}
func main() {
	var cat1 Cat 
	cat1.Name = "小花"
	cat1.Age = 2
	cat1.Color = "pink"
	cat1.Hobby = "吃🐟"
	fmt.Println(cat1)
}
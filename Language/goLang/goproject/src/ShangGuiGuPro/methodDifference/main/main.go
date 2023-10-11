package main

import "fmt"

type Person struct {
	Name string
}

func test01(p Person) {
	fmt.Println(p.Name)
}
func main() {
	p := Person{"鸢飞鱼跃"}
	test01(p)
	//test01(&p)//错误
}
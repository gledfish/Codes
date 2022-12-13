package main

import (
	"fmt"
)

type Person struct {
	Name string
}


func (person Person) test() {
	fmt.Println("test() = ", person.Name)
}

func (person Person) speak() {
	fmt.Println(person.Name, "是一个好人。")
}

func (person Person) calculate(num int) (num2 int) {
	sum := 0
	for  i := 1; i <= num; i++ {
		sum += i
	}
	return sum
}

func main() {
	var person Person
	person.Name = "GledFish"
	person.speak()
	num := 0
	fmt.Println("请输入一个数字：")
	fmt.Scanln(&num)
	fmt.Println(person.Name, "计算的结果是", person.calculate(num))
}
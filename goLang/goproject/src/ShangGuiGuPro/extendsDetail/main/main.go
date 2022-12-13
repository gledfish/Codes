package main

import "fmt"

type A struct {
	Name string
	age int
}

func (a *A) SayOk() {
	fmt.Println("A Sayok", a.Name)
}

func (a *A) hello() {
	fmt.Println("A hello", a.age)
}

type B struct {
	A 
	Name string
}

func (b * B) SayOk() {
	fmt.Println("B Sayok", b.Name)
}
func (b *B) hello() {
	fmt.Println("B hello", b.Name)
}
func main() {
	// var b B
	// b.A.Name = "tom"
	// b.A.age = 19
	// b.A.SayOk()
	// b.A.hello()

	var b B
	b.Name = "jack"
	b.age = 100
	b.SayOk()
	b.hello()
}


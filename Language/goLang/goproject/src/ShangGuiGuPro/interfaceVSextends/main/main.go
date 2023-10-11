package main

import (
	"fmt"
)

type Monkey struct {
	Name string
}

func (this *Monkey) climbing() {
	fmt.Println(this.Name,"生来会爬树。")
}

type BirdAble interface {
	Flying()
}

type LittleMonkey struct {
	Monkey//继承
}

func (this *LittleMonkey) Flying() {
	fmt.Println(this.Name,"通过学习，会飞翔。")
}
func main() {
	monkey := LittleMonkey {
		Monkey {
			Name : "悟空",
		},
	}
	monkey.climbing()
	monkey.Flying()
}
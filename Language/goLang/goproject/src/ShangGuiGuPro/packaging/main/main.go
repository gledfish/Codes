package main

import (
	"fmt"
	"ShangGuiGuPro/packaging/model"
)

func main() {
	p := model.NewPerson("smith")
	fmt.Println(*p)
	p.SetAge(80)
	fmt.Println(*p)
	p.SetSal(5000)
	fmt.Println(*p)
}
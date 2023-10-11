package main

import (
	"fmt"
	"ShangGuiGuPro/factory/module"
)

func main() {
	var stu module.student = module.student {"GledFish", 80}
	point := module.NewStudent("tom~", 88.8)
	fmt.Println(stu.module.GetScore())
}
package main
import (
	"fmt"
)

type AInterface interface {
	Say()
}

type Stu struct {
	Name string
}

func (stu Stu) Say() {
	fmt.Println("stu Say()")
}
func main() {
	var stu Stu//结构体变量，实现了Say()
	var a AInterface = stu
	a.Say()
}
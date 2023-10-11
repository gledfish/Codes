package main

import "fmt"

const Row = 8
const Column = 10
type MethodUtils float64

type Calculator struct {
	Num1 float64
	Num2 float64

}

func (calculator *Calculator) Calculate (operator byte) float64 {
	res := 0.0
	switch operator {
		case '+':
			res = calculator.Num1 + calculator.Num2
		case '-':
			res = calculator.Num1 - calculator.Num2
		default :
			fmt.Println("输入运算符错误")
	}
	return res
}
func (M MethodUtils) print1 () {
	for i := 0; i < Row; i++ {
		for j := 0; j < Column; j++ {
			ch := '*'
			fmt.Printf("%c", ch)
		}
		fmt.Println()
	}
}

func (M MethodUtils) print2 (row int, column int) int {
	for i := 0; i < row; i++ {
		for j := 0; j < column; j++ {
			ch := '-'
			fmt.Printf("%c", ch)
		}
		fmt.Println()
	}
	return row * column
}

func (M *MethodUtils) JudgeNum (num int) {
	if num % 2 == 0 {
		fmt.Printf("%d是偶数\n", num)
	} else {
		fmt.Printf("%d是奇数\n", num)
	}
}

func (M MethodUtils) print3 (row int, column int, key string) {
	for i := 0; i < row; i++ {
		for j := 0; j < column; j++ {
			fmt.Printf("%s", key)
		}
		fmt.Println()
	}
}
func main() {
	//var m MethodUtils
	//fmt.Println(m.print2(3, 2))
	//m.JudgeNum(2)
	//m.print3(3, 2, "X")
    var n Calculator = Calculator{1.2, 2.2}
    res := n.Calculate('+')
    fmt.Println(res)
}
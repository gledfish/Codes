package main

import "fmt"

//编写一个函数，判断输入的参数是什么类型
func TypeJudge(items... interface{}){
	for index, value := range items {
		switch value.(type) {
		case bool :
			fmt.Printf("第%v个参数是bool类型，值是%#v\n", index+1, value)
		case float64 :
			fmt.Printf("第%v个参数是float64类型，值是%#v\n", index+1, value)
		case float32 :
			fmt.Printf("第%v个参数是float32类型，值是%#v\n", index+1, value)
		case int, int32, int64 :
			fmt.Printf("第%v个参数是整数类型，值是%#v\n", index+1, value)
		case string :
			fmt.Printf("第%v个参数是string类型，值是%#v\n", index+1, value)
		default:
			fmt.Printf("第%#v个参数类型不确定, 值是%v", index+1, value)
		}
	}
}
func main() {
	var n1 float32 = 1.2
	var n2 float64 = 2.3
	var n3 int = 20
	var name string = "tom"
	address := "北京"
	n4 := 300
	TypeJudge(n1, n2, n3, name, address, n4)
}
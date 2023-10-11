package main

import (
	"fmt"
	//"time"
	"errors"
)
// func test() {
// 	defer func() {
// 		err := recover()//捕获异常
// 		if err != nil {
// 			fmt.Println("err =", err)
// 			fmt.Println("发送邮件给admin@")
// 		}
// 	}()
// 	num1 := 10
// 	num2 := 0
// 	res  := num1 / num2
// 	fmt.Println("res =", res)
// }

func readConf(name string) (err error){
	if name == "config.ini" {
		return nil
	} else {
		return errors.New("读取文件错误...")
	}
}

func test_readConf() {
	err := readConf("config.ini")
	if err != nil {
		//发送错误，终止程序
		panic(err)
	} 
	fmt.Println("test02继续执行...")
}
func main() {
	//test()
	test_readConf()
	fmt.Println("main()下面的代码...")
}
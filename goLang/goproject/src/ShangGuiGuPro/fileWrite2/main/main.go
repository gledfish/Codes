package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	
	//将d:/test.txt文件内容导入到d:/abc.txt
	filepath1 := "d:/test.txt"
	filepath2 := "d:/abc.txt"

	content, err := ioutil.ReadFile(filepath1)
	if err != nil {
		fmt.Println("read file err", err)
		return
	}
	err = ioutil.WriteFile(filepath2, content, 0666)
	if err != nil {
		fmt.Println("write file error = %v\n", err)
	}
	fmt.Println("导入成功")
}
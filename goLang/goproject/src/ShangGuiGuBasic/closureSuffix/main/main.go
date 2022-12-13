package main

import (
	"fmt"
	"strings"
)
func makeSuffix(suffix string) func (fileName string) string {
	return  func(name string) string {
		//如果没有后缀名，加上后缀名，否则就返回原来的名i在
		if strings.HasSuffix(name, suffix) == false {
			return name + suffix
		}

		return name
	}
}
func main() {
	//返回一个闭包
	f := makeSuffix(".jpg")
	fmt.Println("文件名处理后=", f("bird.avi"))
}
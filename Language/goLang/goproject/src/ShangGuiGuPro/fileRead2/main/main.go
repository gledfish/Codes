package main
import (
	"fmt"
	"io/ioutil"
)
func main() {
	file := "d:/test.txt"
	content, err := ioutil.ReadFile(file)
	// 没有打开文件，所以不用关闭文件。
	if err != nil {
		fmt.Printf("read file err = %v", err)
	}
	fmt.Printf("%v", string(content))//默认按[]byte类型输出，需要类型转换

}
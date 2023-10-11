package main
import (
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("d:/test.txt")
	//file被叫做：文件对象，文件指针，文件句柄
	if err != nil {
		fmt.Println("open file err =", err)
	}

	//如果打开成功，看看文件是什么？
	fmt.Printf("file = %s\n", *file)
	//关闭文件
	err = file.Close()
	if err != nil {
		fmt.Println("close file err",err)
	}
}
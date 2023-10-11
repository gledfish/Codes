package main

import (
	"fmt"
	"bufio"
	"os"
)

func main() {
	//创建文件
	filepath := "d:/abc.txt"
	//打开文件
	file, err := os.OpenFile(filepath, os.O_WRONLY | os.O_CREATE, 0666)
	if err != nil {
		fmt.Printf("open file err = %v\n", err)
		return
	}
	//关闭文件
	defer file.Close()
	//写入文件时，使用带有缓存的*write
	write := bufio.NewWriter(file)
	for i := 0; i < 5; i++ {
		write.WriteString("是的，写入成功了。\r\n")
	}
	//writer是带缓存的，因此起初是保存在缓冲区，需要flush方法写入到文件中
	write.Flush()
	fmt.Println("写入成功。")


	//打开一个存在的文件，将原来的内容覆盖成新的内容
	file, err = os.OpenFile(filepath, os.O_WRONLY | os.O_TRUNC, 0666)
	if err != nil {
		fmt.Printf("open file err = %v\n", err)
		return
	}
	//关闭文件
	defer file.Close()
	//写入文件时，使用带有缓存的*write
	//write := bufio.NewWriter(file)
	for i := 0; i < 10; i++ {
		write.WriteString("你好，尚硅谷！\r\n")
	}
	//writer是带缓存的，因此起初是保存在缓冲区，需要flush方法写入到文件中
	write.Flush()
	fmt.Println("重写成功。")

	//打开一个存在的文件，追加新的内容
	file, err = os.OpenFile(filepath, os.O_WRONLY | os.O_APPEND, 0666)
	if err != nil {
		fmt.Printf("open file err = %v\n", err)
		return
	}
	//关闭文件
	defer file.Close()
	//写入文件时，使用带有缓存的*write
	//write := bufio.NewWriter(file)
	for i := 0; i < 10; i++ {
		write.WriteString("你好，尚硅谷！plus\r\n")
	}
	//writer是带缓存的，因此起初是保存在缓冲区，需要flush方法写入到文件中
	write.Flush()
	fmt.Println("追加成功。")
}

package main

import (
	"fmt"
	"io"
	"os"
	"bufio"
)
//编写一个函数，接受两个文件路径

func CopyFile(dst string, src string) (written int64, err error) {
	srcfile, err := os.Open(src)
	if err != nil {
		fmt.Println(err)
	}
	defer srcfile.Close()
	//通过srcfile, 获取到Reader
	reader := bufio.NewReader(srcfile)
	//打开dst
	dstFile, err := os.OpenFile(dst, os.O_WRONLY | os.O_CREATE, 0666)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer dstFile.Close()
	writer := bufio.NewWriter(dstFile)
	return io.Copy(writer, reader)
}
func main(){
	srcfile := "D:/KuGou/ALisa - insomnia (治愈版).mp3"
	dstFile := "d:/abc.mp3"
	_, err := CopyFile(dstFile, srcfile)
	if err == nil {
		fmt.Println("拷贝完成")
	} else {
		fmt.Println(err)
	}
}
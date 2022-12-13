package main
import (
	"fmt"
	"os"
	"bufio"
	"io"
)

func main() {
	file, err := os.Open("d:/test.txt")
	if err != nil {
		fmt.Println("open file err =", err)
	}

	//创建一个*Reader,是带缓冲的，默认缓冲取区是4096
	reader := bufio.NewReader(file)
	for {
		str, err := reader.ReadString('\n')//读到一个换行符结束
		if err == io.EOF {
			break
		}
		fmt.Print(str)
	}
	fmt.Println("文件读取结束")
	err = file.Close()
	if err != nil {
		fmt.Println("close file err=", err)
	}

}
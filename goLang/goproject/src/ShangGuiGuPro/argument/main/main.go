package main
import (
	"fmt"
	"os"
)
func main() {
	fmt.Printf("命令行参数有%#v\n", len(os.Args))
	//遍历切片，得到所有命令行参数
	for i, v := range os.Args {
		fmt.Printf("args[%v] = %v\n", i, v)
	}
	//命令行参数的个数以空格的方式分割
}
package main
import (
	"fmt"
	"flag"
)

func main() {
	//定义变量，接受命令行参数值
	var user string
	var pwd string
	var host string
	var port int

	flag.StringVar(&user, "u", "", "用户名，默认为空")
	flag.StringVar(&pwd, "pwd", "", "密码，默认为空")
	flag.StringVar(&host, "h", "localhost", "主机名，默认为localhost")
	flag.IntVar(&port, "port", 3306, "端口号，默认为3306")

	//转换,（重要）
	flag.Parse()
	//输出结果
	fmt.Printf("user = %v pwd = %v host = %v port = %v", user, pwd, host, port)
}
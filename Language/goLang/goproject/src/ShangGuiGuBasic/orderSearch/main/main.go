package main
import (
	"fmt"
)

func main() {
	var names [4]string = [4] string {"白眉鹰王", "金毛狮王", "紫衫龙王", "青翼蝠王"}
	//names := [4] string{"白眉鹰王", "金毛狮王", "紫衫龙王", "青翼蝠王"}
	var evilName string
	fmt.Println("请输入您猜测的名字：")
	fmt.Scanln(&evilName)
	flag := -1
	for index, _ := range names {
		if names[index] == evilName {
			flag = index
			break
		}
	}
	if flag == -1 {
		fmt.Println("不好意思，没猜对哦")
	} else {
		fmt.Println("猜对了，对应下标为：", flag)
	}
}

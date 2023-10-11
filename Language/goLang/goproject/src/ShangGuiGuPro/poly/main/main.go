package main
import (
	"fmt"
)

type Usb interface {
	Start()
	Stop()
}

type Phone struct {
	name string
}

func (p Phone) Start() {
	fmt.Println("手机开始工作。。。")
}
func (p Phone) Stop() {
	fmt.Println("手机停止工作。。。")
}

type Camera struct {
	name string
}
func (c Camera) Start() {
	fmt.Println("相机开始工作。。。")
}
func (c Camera) Stop() {
	fmt.Println("相机停止工作。。。")
}

func main() {
	//定义一个Usb接口数组,存放Phone和Camera的结构体变量
	var usbArr [3]Usb

	usbArr[0] = Phone{"Vivo"}
	usbArr[1] = Phone{"Oppo"}
	usbArr[2] = Camera{"佳能"}

	fmt.Println(usbArr)
}
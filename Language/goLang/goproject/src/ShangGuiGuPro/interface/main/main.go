package main

import "fmt"

type USb interface {
	Start()
	Stop()
}
type Phone struct {

}
type Camera struct {

}

func (p Phone) Start() {
	fmt.Println("手机开始工作。。。")
}

func (p Phone) Stop() {
	fmt.Println("手机停止工作。。。")
}

func (p Phone) Call() {
	fmt.Println("手机开始呼叫。。。")
}
func (p Camera) Start() {
	fmt.Println("相机开始工作。。。")
}

func (p Camera) Stop() {
	fmt.Println("相机停止工作。。。")
}

type Computer struct {

}

func (copmuter Computer) Working(usb USb) {
	usb.Start()
	usb.Stop()
}
//接收一个接口类型变量，只要实现了Usb接口，指实现Usb接口的所有方法。
func main() {
	computer := Computer{}
	phone := Phone{}
	camera := Camera{}

	computer.Working(phone)
	computer.Working(camera)

	var usb USb = phone
	phone = usb.(Phone)
	phone.Call()

	phone.Call()
}
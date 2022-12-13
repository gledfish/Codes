package main

import (
	"fmt"
	"Project/客户关系管理项目/service"
)
type CustomerView struct {
	//定义必要的字段
	key int//接受用户输入
	loop bool // 表示是否循环的显示主菜单
	customerService *service.CustomerService 
}

func (this *CustomerView) list() {
	customers := this.customerService.List()
	fmt.Println("-----------客户列表-------------")
	fmt.Println("编号\t姓名\t性别\t年龄\t电话\t邮箱")
	for i := 0; i < len(customers); i++ {
		fmt.Println(customers[i].GetInfo())
	}
	fmt.Println("客户列表完成")
} 

//显示主菜单（也可以封装）
func (this *CustomerView) mainMenu() {
	for {
		fmt.Println("------客户信息管理系统------")
		fmt.Println("       1.添加客户")
		fmt.Println("       2.修改客户")
		fmt.Println("       3.删除客户")
		fmt.Println("       4.客户列表")
		fmt.Println("         5.退出")
		fmt.Print("请选择（1-5）：")

		fmt.Scanln(&this.key)
		switch this.key {
		    case 1:
		    	this.customerService.Add()
		    case 2:
		    	this.customerService.Modify()
		    case 3:
		    	this.customerService.Delete()
		    case 4:
		    	this.list()
		    case 5:
		    	fmt.Println("您确定要退出吗？（y/n）")
		    	var choice string
		    	fmt.Scanln(&choice)
		    	if choice == "y" {
		    		this.loop = false
		    	}
		    default :
		    	fmt.Println("你的输入有误，请重新输入：")
		}

		if !this.loop {
			break
		}

	}
	fmt.Println("已成功退出了客户关系管理系统")
}

func main() {
	//在main函数中，创建实例并运行
	customerView := CustomerView{
		key : 0,
		loop : true,
	}
	customerView.customerService = service.NewCustomerService()
	//运行客户管理系统
	customerView.mainMenu()
}

package service

import (
	"Project/客户关系管理项目/model"
	"fmt"
	"strconv"
)

var id int
var name string
var gender string
var  age int64
var phone string
var email string
var flag bool
//该CustomerService对Customer完成操作
type CustomerService struct {
	customers []model.Customer
	//声明一个字段，表示切片含有多少个字段
	//该字段可以作为新客户的id
	customerNum int
}

//工厂模式
func NewCustomerService() *CustomerService {
	CustomerService := &CustomerService{}
	CustomerService.customerNum = 1
	customer := model.NewCustomer(1, "张三", "男", 20, "112", "zs@sohu.com")
	CustomerService.customers = append(CustomerService.customers, customer)
	return CustomerService
}

//返回一个切片，展示客户信息。
func (this *CustomerService) List() []model.Customer {
	return this.customers
}

//往切片中添加客户
func (this *CustomerService) Add() {
	//获取用户输入
	fmt.Println("请输入姓名：")
	fmt.Scanln(&name)
	fmt.Println("请输入性别（男/女）：")
	fmt.Scanln(&gender)
	fmt.Println("请输入年龄：")
	fmt.Scanln(&age)
	fmt.Println("请输入电话：")
	fmt.Scanln(&phone)
	fmt.Println("请输入邮箱：")
	fmt.Scanln(&email)

	customer := model.NewCustomer(this.customerNum+1, name, gender, age, phone, email)
	this.customers = append(this.customers, customer)
	this.customerNum++
}

//修改客户信息
func (this *CustomerService) Modify() {
		fmt.Println("请输入要修改客户的姓名：")
	    fmt.Scanln(&name)
	    i := this.FindName(name)
	    if i != -1 {
	    	var choice string
			fmt.Println("恭喜您找到了该客户。")
			fmt.Println("请修改姓名：如果不修改请输入n")
			fmt.Scanln(&choice)
			if choice != "n" {
				this.customers[i].Name = choice
			}
	        //fmt.Scanln(&this.customers[i].Name)
	        fmt.Println("请修改性别（男/女）：如果不修改请输入n")
	        fmt.Scanln(&choice)
	        if choice != "n" {
	        	this.customers[i].Gender = choice
	        }
	        fmt.Println("请修改年龄：如果不修改请输入n")
	        fmt.Scanln(&choice)
	        if choice != "n" {
	        	this.customers[i].Age, _ = strconv.ParseInt(choice, 10, 0)
	        }
			fmt.Println("请修改电话：")
			fmt.Scanln(&choice)
	        if choice != "n" {
	        	this.customers[i].Phone = choice
	        }
			fmt.Println("请修改邮箱：")
			fmt.Scanln(&choice)
	        if choice != "n" {
	        	this.customers[i].Email = choice
	        }
			fmt.Println("修改成功。")
		} else {
		fmt.Println("对不起，没有找到该客户")
	}
}

//删除用户
func (this *CustomerService) Delete() {
	fmt.Println("请输入要删除客户的姓名：")
	fmt.Scanln(&name)
	index := this.FindName(name)
	if index != -1 {
		fmt.Println("您确定要删除吗？（y/n）")
		var choice string
		fmt.Scanln(&choice)
		if choice == "y" {
			this.customers = append(this.customers[:index],this.customers[index+1:]...)
		    }
		    fmt.Println("删除成功") 
		} else {
		fmt.Println("删除失败，没有找到该客户")
	}
}
//查找客户
func (this *CustomerService) FindName(name string) int {
	index := -1
	for i := 0; i < len(this.customers); i++ {
		if this.customers[i].Name == name {
			index = i
		}
	}
	return index
}
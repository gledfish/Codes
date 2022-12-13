package utils

import (
	"fmt"
	"os"
)
//定义结构体
type FamilyAccount struct {
	//获取用户的输入
    key int

	loop bool
	//定义用户的余额
	balance float64
	//每次收支的金额
	money float64
	//每次收支的说明
	note string
	//定义变量，记录是否有收支
	//收支明细用字符串来记录
	details string
	flag bool
}

func NewFamilyAccount() {
	return &FamilyAccount {
		key :"",
		loop:true,
		balance:0,
		money:0.0,
		note:0.0,
		details:"收支\t账户金额\t收支金额\t说明",
		flag:false,
	}
}
func (this *FamilyAccount) income() {
	fmt.Println("请输入本次收入金额：")
    fmt.Scanln(&this.money)
	this.balance += this.money
	fmt.Println("请输入本次收入说明：")
	fmt.Scanln(&this.note)
	//将收入情况拼接到details变量
	this.details += fmt.Sprintf("\n收入\t%v\t%v\t%v", this.balance, this.money, this.note)
	this.flag = true
}
func (this *FamilyAccount) showDetails() {
	fmt.Println("\n------当前收支明细记录------")
	if this.flag {
		fmt.Println(this.details)
	} else {
		fmt.Println("当前没有收支明细，来一笔吧！")
	}
}

func (this *FamilyAccount) pay() {
	fmt.Println("请输入本次支出金额：")
			fmt.Scanln(&this.money)
			if this.money > this.balance {
				fmt.Println("余额不足")
			} else {
			 this.balance -= this.money
			 fmt.Println("请输入本次支出说明：")
			 fmt.Scanln(&this.note)
			 //将支出情况拼接到details变量
			 this.details += fmt.Sprintf("\n支出\t%v\t%v\t%v", this.balance, this.money, this.note)
			 this.flag = true
			} 
}

func (this *FamilyAccount) exit() {
	fmt.Println("你确定要退出吗？", "请输入y或者n")
			choice := ""
			for{
				fmt.Scanln(&choice)
				if choice == "y" || choice == "n" {
					break
				}
				fmt.Println("请输入正确的选项：", "请输入y或者n")
			}
			if choice == "y" {
				this.loop = false
			}
		    if !this.loop {
		    	fmt.Println("已退出家庭收支软件")
			    os.Exit(1)
		    } 
}

//绑定方法
func (this *FamilyAccount) Mainmenu() {
	for{
		//显示菜单
		fmt.Println("------家庭收支记账软件------")
		fmt.Println("         1 收支明细 ")
		fmt.Println("         2 登记收入")
		fmt.Println("         3 登记支出")
		fmt.Println("         4 退出软件")
		fmt.Println("请选择（1~4）：")

		fmt.Scanln(&this.key)
		switch this.key {
		case 1:
			this.showDetails()
		case 2:
			this.showDetails()
		case 3:
			this.pay()
		case 4:
			this.exit()
}
}
}
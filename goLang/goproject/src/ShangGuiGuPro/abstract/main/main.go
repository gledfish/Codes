package main

import (
	"fmt"
	"ShangGuiGuPro/abstract/model"
)
func main() {
	account := model.NewAccount()
	fmt.Println(*account)
	var username string
	fmt.Scanln(&username)
	account.SetAccountNO(username)
	fmt.Println(*account)
	account.SetPwd("200920")
	fmt.Println(*account)
	account.SetMutlBalance(500)
	fmt.Println(*account)
}
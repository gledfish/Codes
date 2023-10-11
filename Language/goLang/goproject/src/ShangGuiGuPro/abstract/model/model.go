package model

import "fmt"

type account struct {
	accountNo string
	pwd string
	balance int
}

func NewAccount () *account{
	return &account{}
}

func (account1 *account)SetAccountNO (accountNum string) *account {
	if len(accountNum) > 6 && len(accountNum) < 10 {
		account1.accountNo = accountNum
	    return account1
	} else {
		fmt.Println("账号范围不正确。")
		return nil
	}
}

func (account1 *account)SetPwd (pwd string) *account {
	if len(pwd) == 6 {
		account1.pwd = pwd
	    return account1
	} else {
		fmt.Println("密码长度错误")
		return nil
	}
}

func (account1 *account)SetMutlBalance (money int) *account {
	if money > 20 {
		account1.balance += money
	    return account1
    } else {
    	fmt.Println("金额不足")
    	return nil
    }
}
package model


import "fmt"

//声明一个Customer结构体，表示一个客户信息
type Customer struct {
	Id int
	Name string
	Gender string
	Age int64
	Phone string
	Email string
}

//使用工厂模式，返回一个customer实例
func NewCustomer(id int, name string, gender string,
    age int64, phone string, email string ) Customer {
	return Customer{
		Id : id,
		Name : name,
		Gender : gender,
		Age : age,
		Phone : phone,
		Email : email,
	}
}

//格式化返回用户的信息
func (this Customer) GetInfo() string {
	info := fmt.Sprintf("%v\t%v\t%v\t%v\t%v\t%v\t", this.Id, this.Name, this.Gender, this.Age,  this.Phone, this.Email)
	return info
}
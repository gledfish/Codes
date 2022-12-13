package main

import "fmt"

type user struct {
	NickName string
	Passward string
}
func main() {
	var user1 user
	user1 = {
		"鸢飞鱼跃",
		"888888",
	}
	var users = make(map[string]user)
	flag := 0
	for i, v := range users {
		if i == "鸢飞鱼跃" {
			v.Passward = "888888"
			flag = 1
		}
	}
	if flag == 0 {
		users["鸢飞鱼跃"] = user1
	}
	fmt.Println(users)
}
	// //先声明，再make
	// var a map[string]string
	// //在使用map前需要先make,分配数据空间
	// a = make(map[string]string, 1)
	// a["no3"] = "黑旋风"
	// a["no1"] = "宋江"
	// a["no2"] = "吴用"
	// a["no1"] = "吴用"
	// fmt.Println(a)
	// //第二种，短变量声明
	// cities := make(map[string]string, 10)
	// cities["no1"] = "北京"
	// fmt.Println(cities)
	// //第三种，直接赋值
	// var heroes = map[string]string{
	// 	"no1" : "宋江",
	// 	"no2" : "卢俊义",
	// }
	// fmt.Println(heroes)

	// studentSexes := make(map[string]map[string]string)
	// studentSexes["21009201097"] = make(map[string]string)
	// studentSexes["21009201097"]["name"] = "鸢飞鱼跃"
	// studentSexes["21009201097"]["sex"] = "男"
	// studentSexes["21009201097"]["address"] = "陕西西安"
 // 	//fmt.Println(studentSexes)
 // 	//fmt.Println(studentSexes["21009201097"]["address"])
 // 	studentSexes["31009201097"] = make(map[string]string)
	// studentSexes["31009201097"]["name"] = "鸢飞鱼跃"
	// studentSexes["31009201097"]["sex"] = "男"
	// studentSexes["31009201097"]["address"] = "陕西西安"
 // 	for _, value1 := range studentSexes {
 // 		fmt.Println("k1 =", value1)
 // 		for index2, value2 := range value1 {
 // 			fmt.Printf("\t k2 = %#v, v22 = %#v\n", index2, value2)
 // 		}
 // 	}
 // 	fmt.Println("cities有", len(studentSexes), "段。")

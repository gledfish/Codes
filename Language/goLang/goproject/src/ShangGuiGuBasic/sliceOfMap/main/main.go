package main

import "fmt"

func main() {
	//map切片的使用
	//声明map切片
	var monsters []map[string]string
	monsters = make([]map[string]string, 2)
	if monsters[0] == nil {
		monsters[0] = make(map[string]string)
		monsters[0]["name"] = "牛魔王"
		monsters[0]["age"] = "200"
		monsters[0]["sex"] = "男"
	}
	if monsters[1] == nil {
		monsters[1] = make(map[string]string)
		monsters[1]["name"] = "玉兔精"
		monsters[1]["age"] = "500"
		monsters[1]["sex"] = "女"
	}
	//append动态增加
	newMonster := map[string]string {
		"name" : "新的妖怪",
		"age"  :  "200",
	}
	monsters = append(monsters, newMonster)
	for index1, value1 := range monsters {
		fmt.Println(monsters[index1])
		for index2, value2 := range value1 {
			fmt.Println(index2, value2)
		}
	}
}
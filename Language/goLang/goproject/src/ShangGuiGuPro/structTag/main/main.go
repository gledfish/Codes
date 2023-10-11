package main

import (
	"fmt"
	"encoding/json"
)


type Monster struct {
	Name string `json:"name"`
	Age int `json:"age"`
	Skill string `json:"skill"`
}
func main() {
	monster := Monster{"牛魔王", 500, "芭蕉扇"}
	//将monster序列化
	jsonMonster, err := json.Marshal(monster)
	if err != nil {
		fmt.Println("json处理错误 ", err)
	}
	fmt.Println("jsonString =", string(jsonMonster))
}
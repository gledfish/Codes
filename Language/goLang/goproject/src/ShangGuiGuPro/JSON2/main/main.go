package main

import (
	"fmt"
	"encoding/json"
)

type Monster struct {
	Name string
	Age int
	Birthday string
	Sal float64
	Skill string
}

func testStruct() {
	monster := Monster{
		Name:"牛魔王",
		Age : 500,
		Birthday : "2011-11-11",
		Sal : 8000.0,
		Skill : "牛魔",
	}
	//将monster 序列化
	data, err := json.Marshal(&monster)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("序列化后%v\n",string(data))
	//反序列化
	var monster1 Monster
	err = json.Unmarshal([]byte(data), &monster1)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("反序列化后%v\n", monster1)
}

func testMap() {
	var a map[string]interface{}
	a = make(map[string]interface{})
	a["name"] = "红孩儿"
	a["age"] = 30
	a["address"] = "洪洞"

	data, err := json.Marshal(a)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("序列化后%v\n", string(data))
	//反序列化map
	var b map[string]interface{}
	// b = make(map[string]interface{})
	//反序列化map时不需要make分配空间，被封装到unmarshal函数中
	err = json.Unmarshal([]byte(data), &b)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("反序列化后%v\n", b)
}
func main() {
	//序列化
	//testStruct()
	testMap()
}
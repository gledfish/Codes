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
	fmt.Printf("%v\n",string(data))
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
	fmt.Println(string(data))
}
func main() {
	//序列化
	testStruct()
	testMap()
}
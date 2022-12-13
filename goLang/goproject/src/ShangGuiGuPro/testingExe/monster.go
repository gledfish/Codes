package monster

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
)
type Monster struct {
	Name string
	Age int
	Skill string
}

func (this * Monster) Store() bool {
	//序列化
	data, err := json.Marshal(this)
	if err != nil {
		fmt.Println("Marshal err = ", err)
		return false
	}
	//保存到文件
	filePath := "d:/abc.txt"
	err = ioutil.WriteFile(filePath, data, 0666)
	if err != nil {
		fmt.Println(err)
		return false
	}
	return true
}

func (this * Monster) ReStore() bool {
	filePath := "d:/abc.txt"
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		fmt.Println(err)
		return false
	}
	//反序列化
	err = json.Unmarshal(data, this)
	if err != nil {
		fmt.Println(err)
		return false 
	}
	return true
}
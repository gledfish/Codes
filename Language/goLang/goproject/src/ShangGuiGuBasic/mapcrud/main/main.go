package main

import "fmt"

func main() {
	cities := make(map[string]string, 10)
	cities["no1"] = "北京"
	cities["no2"] = "天津"
	cities["no3"] = "上海"
	fmt.Println(cities)
	//增加和修改
	cities["no4"] = "西安"
	fmt.Println(cities)
	//删除
	delete(cities, "no5")
	fmt.Println(cities)
	//查找
	
	for k, v := range cities {
		fmt.Printf("k = %#v, v = %#v\n", k, v)
	}
}
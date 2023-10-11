package main

import (
	"fmt"
	"reflect"
)
type student struct {
	Name string `json:"name" ini:"s_name"`
	Score int   `json:"score" ini:"s_score"`
}

func (s student) Study() string {
	msg := "好好学习，天天向上。"
	fmt.Println(msg)
	return msg
}

func (s student) Sleep() string {
	msg := "好好睡觉，快快长大。"
	fmt.Println(msg)
	return msg
}

func printMethod(x interface{}) {
	t := reflect.TypeOf(x)
	//v := reflect.ValueOf(x)

	fmt.Println(t.NumMethod())
	// for i := 0; i < v.NumMethod(); i++ {
	// 	methodType := v.Method(i).Type()
	// 	fmt.Printf("method name:%s\n", t.Method(i).Name)
	// 	fmt.Printf("method:%s\n", methodType)

	// 	var args = []reflect.Value{}
	// 	v.Method(i).Call(args)//调用方法
	// }
	//通过方法名获取结构体的方法
	methodobj, err := t.MethodByName("sleep")
	fmt.Println(methodobj.Type())
}
func main() { 
	stu1 := student {
		Name: "小王子",
		Score:90,
	}

	// //通过反射获取结构体中的所有字段信息
	// t := reflect.TypeOf(stu1)
	// //fmt.Printf("name:%v kind:%v\n", t.Name(), t.Kind())

	// // for i := 0; i < t.NumField(); i++ {
	// // 	//i是结构体字段的索引
	// // 	fieldObj := t.Field(i)
	// // 	fmt.Printf("name:%v type:%v tag:%v\n",fieldObj.Name, fieldObj.Type, fieldObj.Tag)
	// //}
	// //根据名字取字段
	// fieldObj2, ok := t.FieldByName("Score")
	// if ok {
	// 			fmt.Printf("name:%v type:%v tag:%v\n",fieldObj2.Name, fieldObj2.Type, fieldObj2.Tag)
//}
printMethod(stu1)
}
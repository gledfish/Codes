//多语言之间交流的数据格式JSON
package main

import (
	"fmt"
	"encoding/json"
)
type Student struct {
	ID int
	Name string
}
//student函数
func newStudent(id int, name string) Student{
	return Student {
		ID: id,
		Name:name,
	}
}
type class struct {
	Title string `json:"title"`
	Students []Student
}
func main() {
	//创建一个班级变量
	c1 := class {
		Title:"火箭101",
		Students : make([]Student, 0, 20),
	}
	//往班级中添加学生
	for i := 0; i < 10; i++ {
		tmpStu := newStudent(i+1, fmt.Sprintf("stu%02d", i+1))
		c1.Students = append(c1.Students, tmpStu)
	}
	data, err := json.Marshal(c1)
	if err != nil {
		fmt.Println("json marshal failed, err:", err)
		return
	} 
	 fmt.Printf("%T\n", data)
	// fmt.Printf("%s\n", data)

	//Json反序列化：满足JSON格式的字符串->go语言中数据
	//jsonStr := `{"Title":"火箭101","Students":[{"ID":1,"Name":"stu01"}]}`
	var c2 class
	err = json.Unmarshal([]byte(data), &c2)
	if err != nil {
		fmt.Println()
		return 
	}
	fmt.Printf("%#v", c2)
}
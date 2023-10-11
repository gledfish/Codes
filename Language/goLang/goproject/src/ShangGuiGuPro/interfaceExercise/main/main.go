package main

import (
	"fmt"
	"sort"
	"math/rand"
)

type Student struct {
	Name string
	Age int
	Score int
}
type studentSlice []Student
//实现interface接口

func (sl studentSlice) Len() int {
	return len(sl)
}
//Less方法决定使用什么标准排序
//1.按Hero的年龄从小到大排序
func (sl studentSlice) Less(i, j int) bool {
	return sl[i].Score > sl[j].Score
}

func (sl studentSlice) Swap(i, j int) {
	// temp := hs[i]
	// hs[i] = hs[j]
	// hs[j] = temp

	sl[i], sl[j] = sl[j], sl[i]
}
func main() {
	var students studentSlice
	for i := 0; i < 10; i++ {
		student := Student{
			Name : fmt.Sprintf("学生%d", rand.Intn(100)),
			Age : rand.Intn(100),
			Score : rand.Intn(150),
		}
		students = append(students, student)
	}
	//测试
	// for _, value := range heroes {
	// 	fmt.Println(value)
	// }
	//调用sort.Sort
	sort.Sort(students)
	for _, value := range students {
		fmt.Println(value)
	}
}

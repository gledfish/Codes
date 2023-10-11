package main

/**学员信息管理系统
 * 需求分析：
 * 1.添加学员信息
 * 2.编辑学员信息
 * 3.展示所有学员信息
 * 4.退出系统
 **/
import (
	"Project/学员信息管理系统/student"
	"fmt"
	"os"
)

func showMenu() {
	fmt.Println("欢迎来到学员管理系统")
	fmt.Println("1.添加学员")
	fmt.Println("2.编辑学员信息")
	fmt.Println("3.展示所有学员信息")
	fmt.Println("4.退出系统")
}

func main() {
	var students []student.Student
	students = make([]student.Student, 0)
	for {
		//1.打印系统菜单
		showMenu()
		//2.等待用户选择要执行的选项
		var choice byte
		fmt.Println("请输入要执行的选项：")
		fmt.Scanln(&choice)
		//3.执行用户操作
		switch choice {
		case 1:
			student.AddStudent(students)
		case 2:
			student.ModityStudent(students)
		case 3:
			for _, v := range students {
				fmt.Println(v)
			}
		case 4:
			os.Exit(1)
		}
	}
}

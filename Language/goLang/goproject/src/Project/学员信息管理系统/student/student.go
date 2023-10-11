package student

type Student struct {
	Id int
	Name string
	Class string
}

func NewStudent(id int, name, class string) *Student {
	return &Student{
		Id : id,
		Name : name,
		Class : class,
	}
}

func AddStudent(students []student.Student) {
	        fmt.Println("请输入学员id：")
			var id int
			fmt.Scanln(&id)
			fmt.Println("请输入学员姓名：")
			var name, class string
			fmt.Scanln(&name)
			fmt.Println("请输入学员班级：")
			fmt.Scanln(&class)
			p := student.NewStudent(id, name, class)
			students = append(students, *p)
			fmt.Println("添加成功")
}

func ModityStudent(students []student.Student) {
	fmt.Println("请输入要修改的学员的id：")
			idTemp := 0
			fmt.Scanln(&idTemp)
			for _, v := range students {
				if v.Id == idTemp {
					fmt.Println("恭喜你找到了。")
					fmt.Println("请输入新的名字：")
					fmt.Scanln(&v.Name)
					fmt.Println("请输入新的id：")
					fmt.Scanln(&v.Id)
					fmt.Println("请输入新的班级：")
					fmt.Scanln(&v.Class)
					fmt.Println("恭喜您修改成功")
					fmt.Println(v)
				} else {
					fmt.Println("对不起，没找到该学员")
				}
			}
}
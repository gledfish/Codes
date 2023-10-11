package main

import "fmt"
 
type Student struct {
	Name string
	Age int
	Score int
}

type Pupil struct {
	Student
}
type Graduate struct {
	Student
}
func (p *Student) ShowInfo() {
	fmt.Printf("%v %v %v\n", p.Name, p.Age, p.Score)
}

func (p *Student) SetScore (score int) {
	p.Score = score
} 

func (p *Pupil) testing() {
	fmt.Println("小学生正在考试中......")
}

func (p *Graduate) testing() {
	fmt.Println("大学生正在考试中......")
}
func main() {
	pupil := &Pupil{}
	pupil.Student.Name = "tom"
	pupil.Student.Age = 10
	pupil.testing()
	pupil.Student.SetScore(70)
	pupil.Student.ShowInfo()

	
}

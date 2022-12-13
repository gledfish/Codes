package main

import ("fmt")

type Circle struct {
	radius float64
}


func (c *Circle) area() float64 {
	c.radius = 10.0
	return 3.14 * c.radius * c.radius
}

type integer int

type Student struct {
	Name string
	Age int
}

func (stu *Student) String() string {
	str := fmt.Sprintf("Name = %v Age = %v", stu.Name, stu.Age)
	return str
}
func (i integer) print1() {
	fmt.Println("i =", i)
}  
func main() {
	var c Circle
	c.radius = 5.0
	res := c.area()
	fmt.Println("面积是：", res)
	fmt.Println(c.radius)

	var num integer
	num = 1
	num.print1()

    stu  := Student {"鸢飞鱼跃", 19}
	fmt.Println(stu.String())
}
package utils

var Age int 
var Name string
//Age和Name需要在main.go中使用，但需要初始化

func init() {
	Age = 100
	Name = "Tom"
}
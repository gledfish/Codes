package main
//reflect demo
import (
	"fmt"
	"reflect"
)

func reflectType (x interface{}) {
	//1.通过类型断言
	//2.借助反射
	obj := reflect.TypeOf(x)
	fmt.Println(obj, obj.Name(), obj.Kind())
	fmt.Printf("%T\n", obj)
	objv := reflect.ValueOf(x)
	fmt.Println(objv)
}

type Cat struct {

}

type Dog struct {

}
func main() {
	var a float32 = 12.34
	reflectType(a)
	var b int8 = 1
	reflectType(b)
	var c Cat
	var d Dog
	reflectType(c)
	reflectType(d)
}
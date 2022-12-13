package main

import "fmt"

type Visitor struct {
	Age int
} 

func (visitor *Visitor) Say() (payment int) {
	for {
		if visitor.Age > 18 {
		payment = 20
		break
	} else if visitor.Age == 'n'{
		break
	} else {
		payment = 0
		break
	}
	}
	return payment
}
func main() {
	var visitor Visitor = Visitor {80}
	fmt.Printf("您的门票价格为%d元。\n", visitor.Say())
}
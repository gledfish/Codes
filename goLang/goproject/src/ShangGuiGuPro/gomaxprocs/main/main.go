package main

import (
	"fmt"
	"runtime"
	"sync"
)

var wg sync.WaitGroup
func a() {
	for i := 1; i <= 4; i++ {
		fmt.Println("A:", i)
	}
	wg.Done()
}

func b() {
	for i := 1; i <= 4; i++ {
		fmt.Println("B:", i)
	} 
	wg.Done()
}
func main() {
	runtime.GOMAXPROCS(2)//只占用二个cpu核心
	wg.Add(2)
	go a()
	go b()
	wg.Wait()
}
package main

import (
	"fmt"
	"io"
	"bufio"
	"os"
)

type CharCount struct {
	chCount int
	NumCount int
	SpaceCount int
	OtherCount int
}
func main() {
	fileName := "d:/abc.txt"
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
		return 
	}
	//创建实例
	var count CharCount
	//创建一个Reader
	reader := bufio.NewReader(file)

	for {
		str, err := reader.ReadString('\n')
		str1 := []rune(str)
		for _, v := range str1 {
			switch {
			case v >= 'a' && v <= 'z' :
				fallthrough
			case v >= 'A' && v <= 'Z' :
				count.chCount++
			case v == ' ' || v == 't' :
				count.SpaceCount++
			case v >= '0' && v <= '9' :
				count.NumCount++
			default:
				count.OtherCount++
			}
		}
		fmt.Println()
		if err == io.EOF {
			break
		}
	}
	fmt.Printf("字符的个数:%#v 数字的个数为%#v 空格的个数为%#v 其他字符的个数为%#v", count.chCount, count.NumCount, count.SpaceCount, count.OtherCount )
}
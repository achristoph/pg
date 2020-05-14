package main

import (
	"fmt"
)

type Color int

const (
	Red Color = iota
	Green
	Blue
)

func main() {
	fmt.Println("there is no enum type in Go. Create a list of consts with iota for sequential integer")
	fmt.Println(Red, Green, Blue)
	var d Color = 0
	fmt.Print(d)
	switch d {
	case Red:
		fmt.Println(" goes up.")
	default:
		fmt.Println(" stays put.")
	}
}

package main

import "fmt"

func main() {
	fmt.Println("iterate map")
	m := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
	}

	for k, v := range m {
		fmt.Println(k, v)
	}

	fmt.Println("golang does not have Set in its standard library. Use map with a constant value to create a set")
	const t = true
	set := map[string]bool{"one": t, "two": t, "three": t}
	fmt.Println(set)
}

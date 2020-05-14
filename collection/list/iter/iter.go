package main

import "fmt"

func main() {
	fmt.Println("iterate list")
	numbers := []int{10, 2, 3}

	for _, e := range numbers {
		fmt.Println(e)
	}

	fmt.Println("iterate with index and value")
	for i, e := range numbers {
		fmt.Println(e, i)
	}

	fmt.Println("iterate list with index")

	for i := 0; i < len(numbers); i++ {
		fmt.Println(numbers[i])
	}

	sum := 0
	fmt.Println("while loop")
	for sum < 3 {
		sum++
	}
	fmt.Println(sum)
}

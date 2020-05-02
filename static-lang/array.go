package main

import (
	"fmt"
	"sort"
	"strings"
)

type byLength []string

func (s byLength) Len() int {
	return len(s)
}

func (s byLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s byLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

type byLowerCase []string

func (s byLowerCase) Len() int {
	return len(s)
}

func (s byLowerCase) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s byLowerCase) Less(i, j int) bool {
	return strings.ToLower(s[i]) < strings.ToLower(s[j])
}

type byLengthThenLowerCase []string

func (s byLengthThenLowerCase) Len() int {
	return len(s)
}

func (s byLengthThenLowerCase) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s byLengthThenLowerCase) Less(i, j int) bool {
	if len(s[i]) < len(s[j]) {
		return true
	}
	if len(s[i]) > len(s[j]) {
		return false
	}
	return strings.ToLower(s[i]) < strings.ToLower(s[j])
}

func main() {

	a := []string{"Art", "b", "ART"}
	c := make([]string, len(a))
	copy(c, a)

	// 1. Creating a new sorted array with a comparator
	sort.Sort(byLowerCase(a))
	sort.Sort(byLength(a))
	sort.Sort(byLengthThenLowerCase(a))
	fmt.Println(a)
	fmt.Println(c)
	// sort.Slice(a, func(i, j int) bool {
	// 	return len(a[i]) < len(a[j])
	// })
	x := []int{1, 2, 3, 4}
	fmt.Println(x[2:4])
}

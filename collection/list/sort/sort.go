package main

import (
	"fmt"
	"sort"
	"strconv"
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
	b := make([]string, len(a))
	copy(b, a)

	// 1. Creating a new sorted array with a comparator
	sort.Sort(byLowerCase(b))
	fmt.Println(b)

	// # 2. Modify current array with multiple comparators
	sort.Sort(byLengthThenLowerCase(a))
	fmt.Println(a)

	// # 3. Sorting array with in-place sort
	sort.Slice(a, func(i, j int) bool {
		return len(a[i]) < len(a[j])
	})
	fmt.Println(a)

	// # 4. Sorting numeric array to string order
	d := []int{2, 100, 3}
	sort.Slice(a, func(i, j int) bool {
		return strconv.Itoa(d[i]) < strconv.Itoa(d[j])
	})
	fmt.Println(d)

	// 5. Sorting string array to numeric order
	e := []string{"2", "100", "3"}
	sort.Slice(e, func(i, j int) bool {
		ei, _ := strconv.Atoi(e[i])
		ej, _ := strconv.Atoi(e[j])
		return ei < ej
	})
	fmt.Println(e)

	// 6. Sorting numeric array
	f := []int{3, 1, 2}
	sort.Slice(f, func(i, j int) bool {
		return f[i] < f[j]
	})
	fmt.Println(f)

}

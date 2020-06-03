//Python is a strongly-typed language under the hood, which means
//that the types of values matter, especially when we're trying
//to perform operations on them.

//Note that if you try running the following code without making any
//changes, you'll get a TypeError saying you can't perform an operation
//on a string and an integer.

//x = 5
//y = "7"

//Write a print statement that combines x + y into the integer value 12
//Write a print statement that combines x + y into the string value 57
//YOUR CODE HERE


package main

import (
	"fmt"
	"strconv"
	)

func main() {
	const x = 5
	var y string = "7"
	
	i1, err := strconv.Atoi(y)
	if err == nil {
		fmt.Println(i1 + x)
	}
	
	i2 := strconv.Itoa(x)
	fmt.Println(i2 + y)
	}
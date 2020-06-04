//For the exercise, look up the methods and functions that are available for use
//with Python lists.

//x = [1, 2, 3]
//y = [8, 9, 10]

//For the following, DO NOT USE AN ASSIGNMENT (=).

//Change x so that it is [1, 2, 3, 4]
//YOUR CODE HERE
//print(x)
//Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
//YOUR CODE HERE
//print(x)

//Change x so that it is [1, 2, 3, 4, 9, 10]
//YOUR CODE HERE
//print(x)

//Change x so that it is [1, 2, 3, 4, 9, 99, 10]
//YOUR CODE HERE
//print(x)

//Print the length of list x
//YOUR CODE HERE

//Print all the values in x multiplied by 1000
//YOUR CODE HERE

package main

import (
	"fmt"
	//"math"
)

func main() {

	x := [] int {1, 2, 3}
	y := [] int {8, 9, 10}
	
	fmt.Println("Original x: ", x)
	fmt.Println("Original y: ", y)
	fmt.Println("")
	
	
	x = append(x, 4)
	fmt.Println("Append 4 to x: ", x)
	
	
	x = append(x, y...)
	fmt.Println("Append y to x: ", x)
	
	i := 4 // Index of item "8"
	x = append(x[:i], x[i+1:]...)
	fmt.Println("Remove 8 from x: ", x)
	
	j := 5 // Index of new item "99"
	x = append(x, 0)
	copy(x[j+1:], x[j:])
	x[j] = 99
	fmt.Println("Insert 99 into x: ", x)
	
	fmt.Println("Length of x: ", len(x))
	
	for k, _ := range x {
		x[k] = x[k] * 1000
	}
	
	fmt.Println("Magnitude 1000 x: ", x)
}








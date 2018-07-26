package main

import (
	"fmt"
	"math"
)

func helloWorld() {
	fmt.Println("Hello, world.")
}

func power(x float64, y float64) float64 {
	return math.Pow(x, y)
}

func main() {
	helloWorld()
	power(2, 65536)
}

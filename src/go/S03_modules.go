//In this exercise, you'll be playing around with the sys module,
//which allows you to access many system specific variables and
//methods, and the os module, which gives you access to lower-
//level operating system functionality.


package main

import (
	"fmt"
	"os"
	"os/user"
	"runtime"
	)
	
func main() {
	argsWithProg := os.Args // Without prohram name: argsWithoutProg := os.Args[1:]
	user, err := user.Current()
	
	if err != nil {
        panic(err)
    }


	fmt.Println("Print out the command line arguments in sys.argv, one per line:", argsWithProg) //Print out the command line arguments in sys.argv, one per line
	fmt.Println("Print out the OS platform you're using:", runtime.GOOS) //Print out the OS platform you're using
	fmt.Println("Print out the version of Go you're using:", runtime.Version()) //Print out the version of Go you're using
	fmt.Println("Print the current process ID:", os.Getpid()) //Print the current process ID
	fmt.Println(os.Getwd()) //Print the current working directory (cwd)
	fmt.Println("Username:", user.Username) //Print out your machine's login name
	
	
	}
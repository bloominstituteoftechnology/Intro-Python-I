## Stretch Goals

# 1. One of Python's main philosophical tenets is its emphasis on readability. To
#    that end, the Python community has standardized around a style guide called
#    [PEP 8](https://www.python.org/dev/peps/pep-0008/). Take a look at it and
#    then go over the code you've written and make sure it adheres to what PEP 8
#    recommends. Alternatively, PEP 8 linters exist for most code editors (you can
#    find instructions on installing a Python linter for VSCode
#    [here](https://code.visualstudio.com/docs/python/linting)). Try installing
#    one for your editor!

# 2. Rewrite code challenges you've solved before or projects you've implemented
#    before in a different language in Python. Start getting in as much practice
#    with the language as possible!

# 3. Write a program to determine if a number, given on the command line, is prime.

#    1. How can you optimize this program?
#    2. Implement [The Sieve of
#       Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#       of the oldest algorithms known (ca. 200 BC).

# input from user 
number = int(input("Enter number: "))

# prime number is alwasy > 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")
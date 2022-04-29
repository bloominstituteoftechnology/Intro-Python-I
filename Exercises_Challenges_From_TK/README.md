# Demonstrate Mastery

> To demonstrate mastery of this module, you need to complete and pass a code review on each of the following:

## Objective challenge:

### Exercise 1

> Start the Python interpreter and use it as a calculator.

> How many seconds are there in 21 minutes and 15 seconds?
```python
print("There are this many seconds",21*60+15)
```
> How many miles are there in 5 kilometers?
```python
print("There are ",5* 0.62137, "miles in 5 kilometers")
```
> If you run a 5 kilometer race in 21 minutes and 15 seconds, what is your average pace (time per mile in minutes and seconds)?
```python
def avg_pace():
    seconds_per_kilometer=(21*60+15)/5
    minutes =seconds_per_kilometer/60
    print("Your average pace is", minutes, "minutes per kilometer")
```
> What is your average speed in miles per hour?

```python
def avg_pace_miles():
    seconds_per_mile=(21*60+15)/(5* 0.62137)
    minutes = seconds_per_mile/60
    new_minutes= str(round(minutes, 2))
    print("Your average pace is", new_minutes, "minutes per mile")
```

> Suppose the cover price of a book is $19.95, but bookstores get a 25% discount. Shipping costs $2.50 for the first copy and $1 
>for each additional copy. What is the total wholesale cost for 75 copies?
```python
book=19.95
def shipping(num):
    if num == 1:
        num*2.50
    elif num <=1:
        2.50 + (num*1)
    return num
def store_cost(num):
    # Handle the number of books passed in and find how much total the books will cost in the end 
    discount = (book*.25)
    number_of_books = num
    book_price = book
    bookstore_price = book_price-discount
    total_price = bookstore_price * number_of_books
    return round(total_price,2)   
def final_cost():
    # Determine the cost per book
    # store_cost(75)
    # Handle the total shipping price
    # shipping(75)
    # Combine the two and return the amount
    return store_cost(75) + shipping(75)
def wholesale():
    print("The total cost for the 75 books, with a 25% discount comes to", final_cost())
    print("Book Price:", (19.95*.25), "Shipping cost:", 74+2.50, "Store Price: ", ((19.95*.25) * 75), "Total Price:", round((((19.95*.75) * 75) + 74+2.50), 2 ))
```

### Exercise 2

> A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes 
>a function object as an argument and calls it twice:
>
> def do_twice(f):
> """
> Takes a function and executes it twice.
> """
> f()
> f()
> Here’s an example that uses do_twice to call a function named print_spam twice:
>
> def print_spam():
> print('spam')

> do_twice(print_spam)
> Type this example into a script and test it.
> Change do_twice so it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
```python
def do_twice(f, location):
    name = input("What is your name? ")
    f(location, name)
    f(location, name)
    
def remind_me_because_im_old(location, name):
    print(f"Silly you, your name is {name}, and you are at {location}")
```

> Define a function called print_twice that takes one argument and prints the value of that argument twice.
```python
def print_twice(user_input):
    print("Earth to Major Tom - This just in: ", user_input, "I repeat", user_input)
```

> Use the changed version of do_twice to call print_twice twice, passing 'spam' as an argument.
```python
def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(argwed):
    print("Earth to Major Tom - This just in: ", argwed, "I repeat", argwed)
```


> Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as 
>a parameter. There should be only two statements in the body of this function, not four.
```python
def do_four(f, arg):
    for x in range (0,4):
        f(arg)
```

    
### Exercise 3

> Fermat’s Last Theorem says that there are no positive integers a, b, and c such that

> a**n + b**n == c\*\*n
> for any values of n greater than 2.
>
> Write a function named check_fermat that takes four parameters—a, b, c and n —and checks to see if Fermat’s theorem holds. If n is 
>greater than 2 and a**n + b**n = c\*\*n the program should print, "Holy smokes, Fermat was wrong!" Otherwise the program should print, 
>"No, that doesn't work."
> Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check 
>whether they violate Fermat’s theorem.

### Objective challenge:

> As you write Python programs, it is important to know when to use a certain data structure and when to use something else. Write out 
>an explanation of when and why you would use each data structure: a list, a dictionary, a tuple, and a set.

### Objective challenge:

> Complete the following either in a python script file or directly in the python interpreter:

### Lists

#### Create a list

> Access list items
> Change the value of a list item
> Loop through a list
> Check if a list item exists
> Get the length of a list
> Add an item to the end of a list
> Add an item at a specified index
> Remove an item
> Remove an item at a specified index
> Empty a list
> Use the list() constructor to make a list

### Dictionaries

#### Create a dictionary

> Access the items of a dictionary
> Change the value of a specific item in a dictionary
> Print all key names in a dictionary, one by one
> Print all values in a dictionary, one by one
> Use the values() function to return values of a dictionary
> Loop through both keys and values, by using the items() function
> Check if a key exists
> Get the length of a dictionary
> Add an item to a dictionary
> Remove an item from a dictionary
> Empty a dictionary
> Use the dict() constructor to create a dictionary

### Tuples

#### Create a tuple

> Access tuple items
> Change tuple values
> Loop through a tuple
> Check if a tuple item exists
> Get the length of a tuple
> Delete a tuple
> Use the tuple() constructor to create a tuple

### Sets

#### Create a set

> Loop through a set
> Check if an item exists
> Add an item to a set
> Add multiple items to a set
> Get the length of a set
> Remove an item in a set
> Remove an item in a set by using the discard() method
> Remove the last item in a set by using the pop() method
> Empty a set
> Delete a set
> Use the set() constructor to create a set

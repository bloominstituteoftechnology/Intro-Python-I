from math import ceil
print("This is roughly equivalent to a console.log")
print("hello world")

print("")

print("Prints a variable value")
name = "Michael"
print(name)

print("")

print("This is a demo of string concatonation")
greeting = "Hello, "
print(greeting + name)

print("")

print("This is an f string, a type of string interpolation")
print(f"String interpolation, {name}")

print("")

print("Use this to view methods")
print(dir("hello"))

print("")

print("Example of the islower method, returns a boolean")
print("hello".islower())

print("")

print("The upper() method is foR YELLING")
print("hello".upper())

print("")

print("The startswith method returns a boolean")
print("hello".startswith("e"))
print("hello".startswith("h"))

print("")

print("This is how you start a list ( array )")
my_list = []
my_list = list()
print(my_list)

print("")

print("To add to a list, use the .append() method")
my_list.append(greeting)
my_list.append(name)
print(my_list)

print("")

print("You can also initialize a list with variables in it")
print("You can also reassign vars, you can overwrite them")
my_list = ["I", "have", "value"]
print(my_list)

print("")

print("To print one at a time, use a for loop")
print("In this case, word is equal to the current index")
for word in my_list:
    print(word)

print("")

print("Multi line comments are done with three double quotes")
print("And single line comments are done with an octothorpe")

print("")

print("To get help with a function, run help(thing)")
print("This is help(range)")
print("Hit Q to close help, or enter to show another line")
print(help(range))

print("")

print("Print the length of a list")
print(len(my_list))

print("")

print("Print the index for each part of length of a list")
print("and prints the var at that index")
for idx in range(len(my_list)):
    print(idx, my_list[idx])

print("")

print("Enumerate does the index and value at the same time")
print("using parenthesis as destructuring")
for (idx, el) in enumerate(my_list):
    print(idx, el)

print("")

print("You can reassign vars at an index simply")
print("by doing list[index] = value")
my_list[2] = "donuts"
print(my_list)

print("")

print("List comprehension: returns something like")
print("give me num multiplied by num for every num in numbers")
print("numbers is the name of the array, the current value is num")
numbers = [1, 2, 3, 4, 5]
squares = [num*num for num in numbers]
print(squares)

print("")

print("A double slash // will round down")
print("where a single slash / is divide")
halves = [num / 2 for num in numbers]
print("halves", halves)
rounded = [num // 2 for num in numbers]
print("rounded", rounded)

print("")

print("To import, mention the place and then the thing")
ceiling = 1.7
print(f"normal: {ceiling} and ceiling: {ceil(ceiling)}")

print("")

print("To print evens, check for modulo of 2 to be 0")
evens = [num for num in numbers if num % 2 == 0]
print(evens)

print("")

print("This will return the name of each person that starts with b")
print("with the first letter capitalized")
print("The name[1:] slices the name starting at index of 1 without end")
names = ["ben", "bob", "barbara", "bart", "joe"]
b_names = [name[0].upper() + name[1:]
           for name in names if name.startswith("b")]
print(b_names)

print("")

print("Or you could do this which is way easier")
print("by utilizing a .capitalize method")
print("remember to check help if you want to see methods")
b_names = [name.capitalize()
           for name in names if name.startswith("b")]
print(b_names)

print("")

print("Strings are immutable, the following won't work")
print("string_example = 'test'")
print("test[0] = 'B'")

print("")

print("You can assign more than one var per line")
print("by saying var, var = value, value")
multi_1, multi_2 = "first", "second"
print(multi_1, multi_2)

print("")

print("Dictionaries are most similar to JS objects")
print("and they are defined with curly brackets")
my_dict = {}
print(my_dict)

print("")

print("They are made up of key value pairs like in JS")
my_dict_keys = {"a": 1, "b": 2}
print(my_dict_keys)

print("")

print("You can assign keys by doing bracket notation like in js")
my_dict_keys['c'] = 3
print(my_dict_keys)

print("")

print("You can also loop over keys")
print("and print type by the type function")
for key in my_dict_keys:
    print(key, type(my_dict_keys[key]))

print("")

print("Lists can have any data type in them")
mixed_list = [1, "2", {"a": 3}]
for item in mixed_list:
    print(item, type(item))

print("")

print("And lists can be reassigned")
mixed_list[0] = "changed"
print(mixed_list)

print("")

print("Tuples are like lists but use parenthesis")
print("and they do not support item assignment.")
print("The following will break")
print("tuple = ('first', 'second', 'third')")
print("tuple[0] = 'error'")

print("")

print("You can check if a key is present in a dictionary")
print("by printing a statement and getting a boolean")
print("a" in my_dict_keys)
print("pizza" in my_dict_keys)

print("")

print("You can create a set with the set function")
print("sets do not allow duplicates")
my_set = set()
my_set.add("a")
print(my_set)
my_set.add("a")
print(my_set)
my_set.add("b")
print(my_set)

print("")

print("You can not change an index of a set")
print("You can remove it and add something else")
my_set.remove("b")
my_set.add("woo")
print(my_set)

print("")

print("Lists: ordered")
print("Dictionaries: not ordered")
print("Sets: not ordered")

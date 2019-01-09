# Write a function called reverseString that accepts a string and returns a reversed copy of the string.

def reverse_string(string):
    reversed = ""
    index = len(string)
    while (index > 0):
        reversed += string[index - 1]
        index -= 1
    return reversed

print(reverse_string("hello world"))
print(reverse_string("asdf"))
print(reverse_string("CS rocks!"))
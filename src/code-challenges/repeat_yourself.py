# Write a method that takes two arguments, a string and a positive integer,
# and prints the string as many times as the integer indicates.

# Input: string and a positive integer
# Output: print the input string repeatedly as the integer indicates

# Example:
# Input: "Hello world", 3
# Output:
#  "Hello world"
#  "Hello world"
#  "Hello world"

# Pseudocode
# START
# # Given a string called words and positive int called num
# WHILE num > 0
#   PRINT words
#   num = num - 1
# END

# Solution 1
def repeat(words, num):
    while num > 0:
        print(words)
        num = num - 1


repeat("Hello world", 3)

# Solution 2
def repeat1(words, num):
    for i in range(num):
        print(words)


repeat1("Hello world1", 3)

# Solution 3
def repeat2(words, num):
    print(f"{words}\n" * num)


repeat2("Hello world2", 3)

# Solution 4
def repeat3(words, num):
    [print(words) for i in range(num)]


repeat3("Hello world3", 3)

# Write a function is_even that will return true if the passed-in number is even.

# def is_even(n):
#   return not n % 2


is_even = lambda n: not n % 2

num = input("Enter a number: ")
num = int(num)

print('{}'.format('Even' if is_even(num) else 'Odd'))
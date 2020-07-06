# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def evenorodds(num):

    even = num % 2

    if even > 0:
        print('The number you enter is ODD')
    else:
        print('The number you enter is EVEN')


numb = int(input('Enter a number: '))
print(evenorodds(numb))

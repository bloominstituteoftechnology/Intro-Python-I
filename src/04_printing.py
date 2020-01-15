"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
#Format String
x = 10
y = 2.24552
z = "I like turtles!"

print('These are my variables:\nx is: % 2d\ny is: %f\nz is: %s' %(x,y,z)) #Using % Operator

print(f'These are my variables:\nx is: {x}\ny is: {y}\nz is: {z}') #Using f-strings

print('These are my variables:\nx is: {0}\ny is: {1}\nz is {2}'.format(x,y,z)) #Using Fortmat


# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
x = 10
y = 2.25
z = "I like turtles!"

print('These are my variables:\nx is: % 2d\ny is: %.2f\nz is: %s' %(x,y,z)) #Using % Operator

# Use the 'format' string method to print the same thing
print('These are my variables:\nx is: {0}\ny is: {1}\nz is: {2}'.format(x,y,z))
# Finally, print the same thing using an f-string
print(f'These are my variables:\nx is: {x}\ny is: {y}\nz is: {z}') #Using f-strings
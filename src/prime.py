# Write a program to determine if a number, given on the command line, is prime.
# Stretch Goals

if num > 1:
for i in range(2, num//2):
if (num % i) == 0:
print(num, "is not a prime number")
break
else:
print(num, "is a prime number")
else:
print(num, "is not a prime number")

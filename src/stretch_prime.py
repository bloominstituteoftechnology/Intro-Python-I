# Check if a number is prime
# --------------------#UPER#--------------------#
# --------------------
# Understand: Have the person enter a number(input), display if the numer is a prime or not(output)
# --------------------
# Plan:
# create input
# if - else to rule out "prime" if number is < 1
# if number is > 1, check for factors
# check for factors with is: x % y == 0
# if number has no factors print "is not a prime"
# if number has factors, print out factors
# --------------------
# Execute:

num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            # iterate through and list out why it's not prime
            print(i, "times", num//i, "is", num)  # 2 x 5 = 10, 5 x 2 = 10

    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")

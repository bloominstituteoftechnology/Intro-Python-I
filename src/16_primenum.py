# Checks a number to see if it's prime
# Code
number = input("Enter a number: ")
number = int(number)


# Method to check Prime Numberr
def check_prime(num):
    prime_numbers = []
    if num > 1:
        for value in range(2, num+1):
            prime = True
            for i in prime_numbers:
                if value % i == 0:
                    prime = False
                    break
            if prime:
                if num == value:
                    return True
                else:
                    prime_numbers.append(value)

if check_prime(number):
    print('Prime!')
else:
    print('Not Prime')

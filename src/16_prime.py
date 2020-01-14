import sys 

def main_fun():
    check_arg()
    num = sys.argv[1]
    # Specifies position of number to check
    check_result(num)

def check_arg():
# Confirms program receives expected arguments
    if len(sys.argv) != 2:
        print('Expected input: python 16_prime.py number')
        sys.exit()

def check_num(num):
# Determines whether the number is prime or not
# Note: prime numbers = greater than 1 and can't be formed by multiplying 2 smaller numbers
    if num < 2:
        return False
    else:
        for i in range(2, num):
        # For inputs in between 2 and whatever the actual number is...
            if num % i ==  0:
                return False 
                # Not prime because this means you could reach num by multiplying a number (i) inside the range
            return True

def check_result(num):
    if check_num(int(num)):
    # Convert to int because inputs are automatically formatted to string
        print(f'{num} is indeed prime.')
    else:
        print(f"Nope, {num} isn't prime.")

main_fun()
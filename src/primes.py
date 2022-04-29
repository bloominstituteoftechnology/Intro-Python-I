from sys import argv

args = argv

arg_count = len(args)
if arg_count != 2:
    raise ValueError('Please provide exactly one integer argument.')

num_to_check = int(args[1])


def is_this_prime(number):
 
    if (number == 1) or (number == 2):
        print(f'The number {number} is prime.')

    else:
  
        for i in range(2, number): # last number in range will actually be number-1
            # print(f'checking {i}')
            if (number % i) == 0:
                print( f'The number {number} is not prime. It is divisible by {i}.')
                break
        else:
            print(f'The number {number} is prime.')


is_this_prime(num_to_check)

# One immediate improvement would be to loop only to the floor of the square root of the
# number being checked.

""" This is a program to find if a number is a prime number or not """

def is_prime(num=3):
    multiples = []
    counter = 2
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                multiples.append(i)
                continue
            else:
                counter += 1
    
        if counter < num:
            print(f'{num} is not prime...')
            print(f'The multiples are: {multiples}')
        else:
            print(f'{num} is PRIME!')
    else: 
        print('Number must be greater than 2')

is_prime(76)

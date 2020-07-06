def is_prime(num: int) -> str:
    if num > 1:
        for i in range(2, num//2):
            if num % i == 0:
                return f'{num} is not prime!'
        return f'{num} is prime!'  
    else:
        return f'{num} is not prime'

while True:
    print("Check if a given number is prime (q) to quit")
    inp = input("Type a number: ")
    
    while not inp.isnumeric() and inp != 'q':
        inp = input("Must be a positive number, try again: ")
    
    if inp == 'q':
        break

    given = int(inp)
    
    print(is_prime(given))
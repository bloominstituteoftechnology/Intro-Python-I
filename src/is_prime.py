def is_prime(num: int) -> str:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return f'{num} is not prime!'
        return f'{num} is prime!'  
    else:
        return f'{num} is not prime'

while True:
    print("Check if a given number is prime (q) to quit")
    inp = input("Type a number: ")
    if inp == 'q':
        break
    while not inp.isnumeric():
        inp = input("Must be a number, try again: ")
    given = int(inp)
    
    print(is_prime(given))
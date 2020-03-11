number = int(input('Please enter a number:'))


i = 2
toggle = 0
while i<number:
    if number%i == 0:
        toggle = 1
        print ("Your number is NOT a prime number!")
        break
    else:
        print ("Your number is a prime number!")
        break
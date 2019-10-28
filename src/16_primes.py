num = int(input("Enter a number: "))


def is_prime(number):
    prime_res = "That IS a Prime Number" 
    non_prime_res = "That is NOT a Prime Number"
    
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, non_prime_res)
                break
        else:
            print(number, prime_res)
    else:
        print(number, non_prime_res)



is_prime(num)



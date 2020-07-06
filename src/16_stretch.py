# Implementing The Sieve of Eratosthenes to determine if a given number is prime


while True:
    num = int(input("Enter a number: "))


    def find_prime(num):
        prime_list = []
        for i in range(2, num+1):
            if i not in prime_list:
                for j in range(i*i, num+1, i):
                    prime_list.append(j)
        if num not in prime_list:
            print("Prime!")
        if num in prime_list:
            print("Not Prime!")


    find_prime(num)


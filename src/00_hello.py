# Print "Hello, world!" to your terminal
print('Hello world')

##stretch goal to find if a number is prime
x = input("Enter an integer to see if it is prime: ")


def isItPrime(n):
    i = 2
    while i <= n:
        if i == n:
            print(f"{n} is prime!")
            return True
        elif n % i == 0:
            print(f"{n} is not prime! it has a lowest demoninator of {i}")
            return False
        else:
            i += 1

isItPrime(int(x))



##implement the sieve of Eratosthenes

def isItPrimeSieve(n):
    prime = [True for i in range(n + 1)]
    a = 2

    while (a * a <= n):
        if(prime[a] == True):
            for i in range(a * 2, n + 1, a):
                prime[i] = False
        a += 1
    
    for a in range(2, n):
        if prime[a]:
            print(a)

    print(n, prime[n])

isItPrimeSieve(int(x))

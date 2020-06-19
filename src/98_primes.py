number = int(input('Please enter a number:'))

def SieveOfEratosthenes(n):
   # array of type boolean with True values in it
   prime = [True for i in range(n + 1)]
   p = 2
   while (p * p <= n):
      # If it remain unchanged it is prime
      if (prime[p] == True):
         # updating all the multiples
         for i in range(p * 2, n + 1, p):
            prime[i] = False
      p += 1
   prime[0]= False
   prime[1]= False
   # Print
   for p in range(n + 1):
      if prime[p]:
         print (p,end=" ")
# main31
if __name__=='__main__':
   n = 33
   print ("The prime numbers smaller than or equal to", n,"is")
   SieveOfEratosthenes(n)


i = 2
toggle = 0
while i<number:
    if number%i == 0:
        toggle = 1
        print ("Your number is NOT a prime number!")
        print(SieveOfEratosthenes(number))
        break
    else:
        print ("Your number is a prime number!")
        print(SieveOfEratosthenes(number))
        break


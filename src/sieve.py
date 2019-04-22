x = input("Enter positive integer to find all primes up to and including the integer: ")

def sieve(num):
  marked = []

  for i in range (2, num + 1):
    if i not in marked:
      print(i)
      for j in range(i*i, num + 1, i):
        marked.append(j)

sieve(x)
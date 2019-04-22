import math

x = input("Enter a number, I'll let you know if it's prime:")

def isPrime(num):
  if num < 2:
    return False

  for i in range(2, math.ceil(math.sqrt(num))):
    if num % i == 0:
      return False

  return True

if isPrime(int(x)):
  print('Prime')
else:
  print('Not prime')

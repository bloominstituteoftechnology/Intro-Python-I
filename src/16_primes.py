n = int(input('Enter an upper limit to search for primes: '))

p = 2

primes = []

dic = {x:False for x in range(p,n)}
for x in dic:
    if(dic[x] == False):
        primes.append(x)
        for loc in range(x+x,n,x):
            dic[loc] = True
    else:
        pass
        
print('Primes Found:')
for x in primes:
    print(x)

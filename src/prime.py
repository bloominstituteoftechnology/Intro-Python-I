# List endofunctor fmap
def listF_map(f, lF):
    if isinstance(lF, tuple):
        return (lF[0], f(lF[1]))
    elif lF is None:
        return None

# List endofunctor in
def list_in(lF):
    if isinstance(lF, tuple):
        r = lF[1].copy()
        r.insert(0, lF[0])
        return r
    elif lF is None:
        return []

# definition of an anamorphism over a coalgebra
def ana(mapF, inF, coalg, a):
    return inF(mapF(lambda x: ana(mapF, inF, coalg, x), coalg(a)))

# coalgebra determining one step of the sieve of ero-something-or-other
def sieve_coalg(l):
    if l == []:
        return None
    else:
        filtered_tail = list(filter(lambda x: x % l[0] != 0, l))
        return (l[0], filtered_tail)

# the sieve itself as an anamorphism of the above coalgebra
def sieve(l):
    return ana(listF_map, list_in, sieve_coalg, l)

# I/O
if __name__ == "__main__":
    inp = int(input("Please, give me a prime!: "))

    if inp < 2:
      print(f"{inp} is not a prime! It's too small!")
    else:
      primes = sieve(range(2, inp+1))

      if inp == primes[-1]:
        print(f"{inp} is a prime! Thank you!")
      else:
        print(f"{inp} is not a prime! Dang you!")

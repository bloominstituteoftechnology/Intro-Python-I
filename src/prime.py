from typing import TypeVar, Generic, List, Callable

A = TypeVar('A')
L = TypeVar('L')
X = TypeVar('X')
Y = TypeVar('Y')

# Endofunctor of a list
class ListF(Generic[A, L]):
    pass

class ConsF(ListF[A, L]):
    def __init__(self, head: A, tail: L) -> None:
        self.head = head
        self.tail = tail
        
    def __str__(self):
        return "ConsF(" + str(self.head) + ", " + str(self.tail) + ")"

class NilF(ListF[A, L]):
    def __init__(self) -> None:
        pass
        
    def __str__(self):
        return "NilF()"

# List endofunctor fmap
def listF_map(f: Callable[[X], Y], lF: ListF[A, X]) -> ListF[A, Y]:
    if isinstance(lF, ConsF):
        return ConsF(lF.head, f(lF.tail))
    elif isinstance(lF, NilF):
        return NilF()

# List endofunctor in/out
def list_in(lF : ListF[A, List[A]]) -> List[A]:
    if isinstance(lF, ConsF):
        r = lF.tail.copy()
        r.insert(0, lF.head)
        return r
    elif isinstance(lF, NilF):
        return []

def list_out(l : List[A]) -> ListF[A, List[A]]:
    if l == []:
        return NilF()
    else:
        l2 = l.copy()
        r = l2.pop(0)
        return ConsF(r, l2)

# definition of an anamorphism over a coalgebra
def ana(mapF, inF, coalg, a):
    return inF(mapF(lambda x: ana(mapF, inF, coalg, x), coalg(a)))

# coalgebra determining one step of the sieve of ero-something-or-other
def sieve_coalg(l: List[int]) -> ListF[int, List[int]]:
    if l == []:
        return NilF()
    else:
        head = l[0]
        tail = l[0:]
        filtered_tail = list(filter(lambda x: x % head != 0, l))
        return ConsF(head, filtered_tail)

# the sieve itself as an anamorphism of the above coalgebra
def sieve(l: List[int]) -> List[int]:
    return ana(listF_map, list_in, sieve_coalg, l)

if __name__ == "__main__":
    inp = int(input("Please, give me a prime!: "))

    if inp < 2:
      print(f"{inp} is not a prime! It's too small!")
    else:
      primes = sieve(range(2, inp+1))

      if inp in primes:
        print(f"{inp} is a prime! Thank you!")
      else:
        print(f"{inp} is not a prime! Dang you!")

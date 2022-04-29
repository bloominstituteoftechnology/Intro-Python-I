"""
Input: number
Output: list of primes
"""
def prime(num):
    try:
        """make a list that start from 2"""
        l = [i for i in range(2,int(num)+1)]
        """make a copy of the list to reference"""
        m = l.copy()
        """k has the posible slices of the initial array"""
        k=[(2,2),(4,3),(8,5),(12,7)]
        for a in k:
            """Go throught the initial array and eliminate the slices"""
            l = [x for x in l if x not in m[a[0]::a[1]]]
        if int(num) in l: print(num,"It's a prime")
        else: print("It's not a prime")
    except:
        print(f'{num} is an invalid input')

num = input('Write a number bigger than 2 to find its primes: ')
prime(num)

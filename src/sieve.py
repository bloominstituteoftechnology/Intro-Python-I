"""
Python implementation of the sieve of Erathosthenes.
"""


def b_dict(number):
    #Creates a boolean dict for the sieve
    keys = [x for x in range(2, number)]
    return dict.fromkeys(keys, True)
    
def sieve(number):
    """
    Returns all the prime numbers up to input value.
    """
    true_dict = b_dict(number)

    for x in range(2, int(number**0.5)+1):

        if true_dict[x] == True:

            for j in range(x*x, number, x):
                true_dict[j] = False

    return [key for key, value in true_dict.items() if value == True]

print('This is a python implementation of the sieve of Erathosthenes.')
user_input = int(input("Please input an integer limit: "))
print('Here are all the prime numbers up to your limit: ')
print(sieve(user_input))

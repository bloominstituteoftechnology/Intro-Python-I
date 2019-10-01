import sys

def is_prime(number):
    baby_comps = [4, 6, 8, 9]
    if number < 10: 
        if number in baby_comps:
            return False
        elif number not in baby_comps:
            return True
    elif number % 2 == 0:
        return False
    elif number % 3 == 0:
        return False
    elif number % 5 == 0:
        return False
    elif number % 7 == 0:
        return False
    else:
        return True

print(is_prime(int(sys.argv[1])))
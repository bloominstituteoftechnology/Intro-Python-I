def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_test(num):
    if is_prime(num):
        print("Prime!")
    else:
        print("Not Prime!")

#prime
print("Prime Numbers:")
prime_test(2)
prime_test(3)
prime_test(5)
prime_test(11)
prime_test(199)
prime_test(197)

#not prime
print("\nNot Prime Numbers:")
prime_test(1)
prime_test(25)
prime_test(6)
prime_test(422)
prime_test(198)
prime_test(36)


import math


def sieve():
    print('Get all of the prime numbers up to a certain number.')
    num = int(input('Enter an integer, probably less than 10001: '))
    num_list = []
    for i in range(2, num + 1):
        num_list.append(i)
    i = 0
    j = 0
    while i <= int(math.sqrt(num)):  # i < len(num_list)
        j = 0
        while j < len(num_list):
            if (num_list[j] % num_list[i] == 0 and num_list[j] != num_list[i]):
                print(f'Time to cross out {num_list[j]}')
                num_list.remove(num_list[j])
            j += 1
        i += 1
    print(num_list)
    return num_list


sieve()

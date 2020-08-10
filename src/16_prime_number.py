import sys

def prime_number(input):
    input = int(sys.argv[1])
    is_number_prime = False
    flag_changed = False
    counter1=1
    counter2=1
    loop_input_size=input-1

    if input == 2 or input == 3:
        is_number_prime=True
        print(is_number_prime)
        return is_number_prime
    if input == 9:
        print(is_number_prime)
        return is_number_prime

    for i in range(counter1, loop_input_size):
        if(flag_changed == True):
            break
        for j in range(counter2, loop_input_size):
            print(is_number_prime, "i:", i, "j:", j)
            if i*j == input and (i != 1 or j != 1):
                is_number_prime = False
                flag_changed = True
                break
            elif i *j > input:
                is_number_prime = True
                flag_changed = True
                break

    print(is_number_prime)
    return is_number_prime

prime_number(42)
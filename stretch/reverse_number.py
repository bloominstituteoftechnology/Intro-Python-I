# Reverse a number


def reverse_num(num):
    # one way to do it haha
    # int(str(num)[::-1])
    # more readable
    string = str(num)
    r_str = string[::-1]
    r_num = int(r_str)
    return r_num


print(reverse_num(56))

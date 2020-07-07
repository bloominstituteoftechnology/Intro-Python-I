def stupid_addition(x, y):
    if type(x) == type(y):
        if type(x) == int:
            return str(x) + str(y)
        elif type(x) == str:
            return int(x) + int(y)
    return None


print(stupid_addition(1, '22'))
print(stupid_addition(3, 5))
print(stupid_addition('33', '22'))

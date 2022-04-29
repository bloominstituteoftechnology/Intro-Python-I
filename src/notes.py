l = [10, 9, 3, 15]

def mult_list(l):
    for i in range(len(l)):
        l[i] *= 2
    return l

mult_list(l)

print(l)
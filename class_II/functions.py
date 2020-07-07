# define a function that multiplies  provided number by 2
def mult2(n):
    return n * 2

l = [10, 9, 8, 15]
# define a function that multiplies every number in a list by 2
def mult2_list(l):
    # iterate through another function
    for item in range(len(l)):
        l[item] *= 2
    return l

print(mult2_list(l))
# passing by ref vs passing by value
# PBR: we have a ref to a list l, we passed into a function
# the function changed the contents of the list
# so even when we exited out of the function, the change persisted

# PBV: the function receives a brand new copy of the data;
# outside the function, the changes that the function makes
# don't persist unless we explicitly save it

# When does PBR happen and when does PBV happen (we don't have
# explicit control over this)

# Typically, we see PBR when we pass "large" things to a 
# function (large being datastructures)

# Do we just pass a ref to the data structure or copy the 
# whole thing? - passing by reference is cheaper
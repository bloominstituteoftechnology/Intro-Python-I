def mult(a): # a = <object>  # a = my_list
    for idx in range(len(a)):
        a[idx] *= 2

my_list = [1,2,3,4]

mult(my_list)
print(my_list)

def rename(a):
    a = None

rename(my_list)
print(my_list)

def mult_one(num):
    num *= 2
    return num

x = 5 
mult_one(x)
print(x)

print(mult_one(x))

x = 5
y = x
y *= 2
print(x)
print(y)

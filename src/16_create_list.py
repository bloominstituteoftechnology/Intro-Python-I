import random

# 1
arr = []
for i in range(10):
    arr.append(random.randint(-25, 25))

print(arr)

# 2
newArr = []
for i in arr:
    if(i < 0):
        newArr.append(i)

print(newArr)

# 3
foods = ("pizza", "sushi", "kimchi")
for food in foods:
    print(food)

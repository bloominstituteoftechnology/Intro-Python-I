print(True, type(True))
print ((1,3), type((1,3)))

print(None)

names=["chirag", "payal"]
lucky_numbers = {
    "p": 1, 
    "b": 5,
    "c": 28 
}

print(lucky_numbers)
for name in names:
    your_lucky_number = f"Hello {name}!, Your lucky number is: {lucky_numbers[name[0].lower()]}"
    print(your_lucky_number)

for x in lucky_numbers.items():
    print(x)

for x in lucky_numbers.values():
    print(x)

def helloFunction(name):
    print(f"Hello {name}")

helloFunction("Bobby")

test =[{"1":3}, {"3":3}]
print(type(test))
test[0]["1"] = 5
print(test)
msg = 'Hello World!'
print(msg)

#---------------------------------------

print('Expected 8: result= ',4 + 4)

#---------------------------------------

print('Expected str: result= ',type(msg))
print('Expected int: result= ',type(4))
print('Expected fload: result= ',type(6.6))
print('Expected bool: result= ',type(True))
print('Expected bool: result= ',type(False))

#---------------------------------------

def print_list(list):
    for item in list:
        print(item)

list = ['Jam', 3, 'bob']

print_list(list)

#---------------------------------------

def print_l():
    print("Oh yeah, I'll tell you something")
    print("I think you'll understand")
    print("Then I'll say that something")
    print("I wanna hold your hand")

print_l()
#---------------------------------------

for i in range(5):
    print('Hello')
#---------------------------------------

# x = input('Enter X: ')
# y = input('Enter Y: ')

# if x < y:
#     print('X is less than Y')
# else:
#     print('X is greather than Y')

#---------------------------------------\

def print_info( name, age):
    name = name
    age = age
     
    print(name, age)

# x = input('Enter X: ')
# y = input('Enter Y: ')
print_info(name ='Hamid', age= 34)

#--------------------------------------- List

names = ['Amin', 'Hamid','Elham']
numbers = [2,1,3]
empty = []

names[0] = 'Azizy'
numbers[1] = 5
empty.append('School')
empty.insert(0,3)
# numbers.reverse()

numbers.sort(reverse=True)
print(names.count('Hamid'))

print(names, numbers, empty)

print('Sum of Numbers =>',sum(numbers))

print('len of numbers =>', len(numbers))

print('Min number in numbers =>', min(numbers))

print('Max number in numbers =>', max(numbers))

names.remove('Hamid')
print('removed from names => ',names)

names.pop(1)
print('pop by index from names =>', names)

#--------------------------------------- Dictionaries

car = {
    'brand': 'Honda',
    'model': 'C',
    'year': 2007
}

def f1(**kwargs):
    for key, value in kwargs.items():
        print(f'key: {key} value: {value}')

f1(**car)
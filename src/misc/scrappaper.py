a = 3
b = "123"
# print(a*b)
c = a * b
# print(c)
# print(a + b)
list1 = [1, 2, 4]
list2 = [1, 3, 5]
# Combine lists so no elements are repeated
# print(list1.extend(list2))
# print(list1.extend([5]))


class Parent(object):
    def fun(self):
        print('Hi!')


class Child(Parent):
    def fun(self):
        print('Bye!')


p = Parent()
p.fun()
c = Child()
c.fun()


class Animal:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender


'''
class Llama(Animal):
    def __init__(self, height, is_domesticated):
        super().__init__(age, gender)
        self.height = height
        self.is_domesticated = is_domesticated

    def __str__(self):
        return f'{self.height} in.tall, {self.is_domesticated}'


my_llama = Llama(4, 'female', 25, True)
# print(my_llama)
'''


class Book:
    def __init__(self, name, year, author_first, author_last):
        self.name = name
        self.year = year
        self.author = Author(author_first, author_last)


class Author:
    def __init__(self, first, last):
        self.first = first
        self.last = last


b = Book('a book', 2020, 'Heather', 'Nuffer')
print(b.author)

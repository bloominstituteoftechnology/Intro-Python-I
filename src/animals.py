from abc import ABC, abstractmethod


class Animal(ABC): #Inheriting from abstract base class and we are going to make this an abstract method
    def __init__(self, name, legs): #Special built-in method; always do 'self" in all classes
        self.name = name
        self.legs = legs
    @abstractmethod #Ensures that each new animal has to have the classifications of speak and species; like a rough template of require things to fill out
    def speak(self): #Creates method speak
        pass
    @abstractmethod #Ensures that each new animal has to have the classifications of speak and species
    def species(self):
        pass


class Dog(Animal): #Making an actual dog; inheriting from animal because dog is a sub-class of animal;
    def __init__(self, name, legs = 4): # dog refers to parent class and can have the attribute .name by passing in the name
        super().__init__(name, legs) #Super is a way of referring to the parent class; takes argument name; has default
                                  # value of 4 for legs

    def speak(self): #Creates method speak
        return 'Woof!'

    def species(self): #Overwrites the parents class's method species
        print('Dog')


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, 2)

    def speak(self): #Creates method speak
        return 'Tweet tweet!'

    def species(self): #Overwrites the parents class's method species
        print('Bird')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 2)

    def speak(self):  # Creates method speak
        return 'Meow!'

    def species(self):  # Overwrites the parents class's method species
        print('Cat')


b = Bird('Larry')
c = Cat('Garfield')
d = Dog('Fido')

animals = [b, c, d]

for animal in animals:
    print(f'{animal.name} says {animal.speak()}')


class Building:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def __repr__(self):
        return self.name

class Room:
    def __init__(self, room_type):
        self.type = room_type

    def __repr__(self):
        return self.type


bedroom = Room('Bedroom')
bathroom = Room('Bathroom')

house = Building('My house', [bedroom, bathroom])

print(house)
print(house.rooms)



# a = Animal('Rover', 5)
# print(a)
# print(a.name)
# print(a.legs)
d = Dog('Fido')
print(d)
print(d.name)
print(d.legs)
d.speak()
d.species() #Inherited from parent class

b = Bird('Larry')
b.speak()
b.species() #Inherited from parent class
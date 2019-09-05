#Inheritance in OOP

class Animal: # Base class, Parent class, Top level class
    def call(self):
        def __init__(self, name):
            
        print("generic animal sound")

class Vertebrate(Animal): # vertebrate "is a" animal
    def call(self):
        print("generic vertebrate sound")
class Mammal(Vertebrate):
    pass
class Cat(Vertebrate):
    def call(self):
        print("Meow")
class Invertebrate(Animal): # Invertebrate "is a" animal
    pass


animals = [
    Animal(),
    Vertebrate(),
    Invertebrate(),
    Cat()
]

for a in animals:
    a.call()
class Animal:   # "Base class"

    def __init__(self, name):
        self.name = name

    def call(self):
        print(f"{self.name}: Generic animal sound")

class Vertebrate(Animal):  # Vertebrate is an Animal, "is-a" relationship

    def call(self):   # Override the parent class's call method
        print(f"{self.name}: Generic vertebrate sound")

class Mammal(Vertebrate):
    pass

class Cat(Mammal):

    def __init__(self, name, evil):
        super().__init__(name)
        self.evil = evil

    def call(self):   # Override the parent class's call method
        print(f'{self.name} ({"evil" if self.evil else "not evil"}): Meow')

class Invertebrate(Animal):  # Invertebrate is an Animal, "is-a" relationship
    pass

animals = [
    Animal("animal 1"),
    Vertebrate("vert 1"),
    Invertebrate("invert 1"),
    Cat("cat 1", False),
]

for a in animals:
    a.call()
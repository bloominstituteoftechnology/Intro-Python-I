class Animal:
    count = 0
    def __init__(self, name, color, height, diet, species, owners):
        self.name = name
        self.color = color
        self.height = height
        self.diet = diet
        self.species = species
        self.owners = owners 
        Animal.count += 1
        #actions
        def speak(self):
            if self.species == "DOG":
                print("woof!")
            else:
                print("what should i do!")
        def eat(self):
            pass
        def sleep(self):
            pass
        def move(self):
            pass

class Dog(Animal):
    def __init__(self, name, color, height, owner):
        super().__init__(name, color, height, "Carnivore", "Dog", owner = None)
        self.owner = owner
    def speak(self):
        print("woof woof")

#class human relation to the pet
class Human:
    def __init__(self, name, pets):
        self.name = name
        self.pets = []
        # if owner dont got pets return an empty list
        if self.pets is None:
            self.pets = []
    
    def add_pet(self, new_pet):
        self.pets.append(new_pet)
        new_pet.owner = self 
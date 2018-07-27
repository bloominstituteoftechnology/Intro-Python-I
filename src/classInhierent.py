# Class Hierarchy
#
# Shows which classes subclass from which other classes:
#
# (Animal)->(Ostrich)
#   |
#   v
# (Goat)->(AngloNubianGoat)->(FaintingGoat)
#   |
#   v
# (AlpineGoat)
#
# Goat is a subclass of Animal
# AlpineGoat is a subclass of Goat... and a subclass of Animal
#
# Animal is the base class
# Animal is a superclass of Goat... and a superclass of FaintingGoat

# Declare the base class, Animal:


class Animal:
    def __init__(self, type):
        self.type = type  # mammal or reptile
        #self.has_called = False

    def call(self):
        #self.has_called = True
        print("[generic animal sound]")

    def run(self):
        print("[generic animal run]")


a = Animal()

# call() is not so exciting. The base class expects subclasses will
# *override* the call method to make it interesting.

a.call()  # [generic animal sound]

# Goat is a subclass
# Animal is the superclass (maybe the "base class")

# Goat is-a Animal
# (As opposed to has-a)


class Goat(Animal):
    def __init__(self):
        super().__init__("mammal")

    # override the call method
    def call(self):
        # Somtimes you want to call the superclass's method if that
        # method provides some functionality that you don't want to
        # duplicate. Other times you don't want to call it, if you're
        # trying to prevent it from executing its usual functionality.
        # The documentation should elaborate on whether or not you want
        # to call the superclass's method.
        # super().call()
        print("BLAAAAAHGGGGGHH!")


# Instantiate (means "create objects from a class") some Goats:

g = Goat()   # We say "g" is an "instance of Goat"
h = Goat()   # We say "h" is an "instance of Goat"
i = Goat()   # We say "i" is an "instance of Goat"

g.call()  # BLAAAAAHGGGGGHH!

# Make a list of all Animals (a is Animal, the rest are Goat)
animals = [a, g, h, i]

# Have them all call!
for a in animals:
    a.call()

# Prints:
#
# [generic animal sound]
# BLAAAAAHGGGGGHH!
# BLAAAAAHGGGGGHH!
# BLAAAAAHGGGGGHH!

# Have them all run!
for a in animals:
    a.run()

# Prints:
#
# [generic animal run]
# [generic animal run]
# [generic animal run]
# [generic animal run]
#
# because Goat did NOT override the run() method

# Detect what class something is at runtime:

print(type(g))  # Goat
print(g.type)   # mammal


def count_goats(animal_list):
    count = 0

    for a in animal_list:
        # if type(a) == Goat:  # specifically a Goat
        if isinstance(a, Goat):  # Goat or subclass of Goat
            count += 1

    return count


print(count_goats(animals))

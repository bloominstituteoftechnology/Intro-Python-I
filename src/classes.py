# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return (f'Name: "{self.name}" - Lat: {self.lat}, Lon: {self.lon}')


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

#f is a simplied version of str.format()
# instead of codeing "Name, {name}".format(name=Waypoint['name'])


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return (
            f'Name: "{self.name}" - Difficulty: {self.difficulty}, Size: {self.size}, Lat: {self.lat}, Lon: {self.lon}'
        )


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint('Catacombs', 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)

# # Animal class from lecture
# class Animal:
#     def __init__(self, name, species, sound, num_legs):
#         self.name = name
#         self.species = species
#         self.sound = sound
#         self.num_legs = num_legs

#     def new_name(self, name):
#         self.name = name

#     def set_num_legs(self, num):
#         self.num_legs = num

#     def make_sound(self):
#         print(self.sound)

# animal_a = Animal("ernie", "elephant", "pbbbbbbbt", 4)

# animal_a.make_sound()
# print(animal_a.name)
# animal_a.new_name('monty')
# print(animal_a.name)
# print(animal_a.num_legs)
# animal_a.set_num_legs(3)
# print(animal_a.num_legs)

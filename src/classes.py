# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        return('Name: ' + self.name + ', Latitude: ' + str(self.lat) + ', Longitude: ' + str(self.lon))



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        return('Name: ' + self.name + ', Difficulty: ' + str(self.difficulty) + ', Size: ' + str(self.size) + ', Latitude: ' + str(self.lat) + ', Longitude: ' + str(self.lon))

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print("%s, %f, %f" % (waypoint.name, waypoint.lat, waypoint.lon) )

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)



# class Animal:
#     # Define attributes
#     def __init__(self, name, sound, species, num_legs=2):
#         self.name = name
#         self.species = species
#         self.num_legs = num_legs
#         self.sound = sound
            
#     # Define class functions
#     def set_num_legs(self, num):
#         self.num_legs = num

#     def make_sound(self):
#         print(self.sound)

# # Instance of class
# animal_a = Animal("ernie", "pbbbt", "elephant", 4)

# animal_a.make_sound()
# print(animal_a.num_legs)
# animal_a.set_num_legs(3)
# print(animal_a.num_legs)


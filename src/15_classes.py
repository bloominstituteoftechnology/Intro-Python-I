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
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    # def __str__(self):
    #     return Waypoint(name= self.name, lat= str(self.lat), lon= str(self.lon))


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    # def __str__(self):
    #     return {'name': self.name, 'difficulty': self.difficulty, 'size': self.size, 'lat': self.size, 'lon': self.lon}
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
x = "Catacombs"
y = 41.70505
z = -121.51521
print(f"Waypoint\'s name is {x} and it is located at latitude: {y} and longitude: {z}.")

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
a = "Newberry Views"
b = 1.5
c = 2
d = 44.052137
e = -121.41556
# Print it--also make this print more nicely
#print(geocache.__str__())
print(f"Geocache\'s name is {a} and it\'s difficulty is {b} and a size {c}. It is located at latitude: {d} and longitude: {e}.")


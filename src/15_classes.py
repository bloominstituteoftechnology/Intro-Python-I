# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return str(self.__dict__)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

x = LatLon(3, 6)

print(x.lat, x.lon)

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name: str, lat: float, lon: float):
        super().__init__(lat, lon)
        self.name = name 

    def __str__(self):
        return str(self.__dict__)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# # YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty: float, size: float, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# I think this is stupid since you'd want the key/val pairs like a normal person
# who follows Python conventions instead of only the values
# YOUR CODE HERE

# note that Waypoint inherits str from LatLon which is quite cool
y = Waypoint("nowhere", 0, 0)

print(y)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(y)
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
z = Geocache(lat=5, lon=20, size=3, difficulty=99, name="geo")
print(z)
# Print it--also make this print more nicely
#print(geocache)

# Make a class LatLon > that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        s = f"Latitude: {self.lat}, Longitude: {self.lon}"
        return s

x = LatLon(2, 3)
print(x)

# test = LatLon(22,23)
# print(test.lon)
# >>> 23 > test Passes

# Make a class Waypoint > that can be passed 3 parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon): 
        super().__init__(lat, lon)
        self.name = name
    
    def __str__(self):
        coordinates = f"Name: {self.name}: Latitude: {self.lat}, Longitude: {self.lon}"
        return coordinates

print(Waypoint(2,3, "isle-island"))


# Make a class Geocache > that can be passed parameters >> `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from? name, lat lon from Waypoint
# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        x = f"Name: {self.name}, Difficulty: {self.difficulty}, Size: {self.size}, Latitude: {self.lat}, Longitude: {self.lon}"
        return x


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE

waypointX = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypointX)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypointX)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
geocacheNV = Geocache("Newberry Views", 1.5,  2, 44.052137, -121.41556)
print(geocacheNV)

# Print it--also make this print more nicely
print(geocacheNV)

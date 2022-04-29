# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

test = LatLon(100, -100)
print(f"Latitude is {test.lat}, Longitude is {test.lon}")

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon ):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"

test2 = Waypoint(14, 13, "David")
print(f"{test2.lat} is lat, {test2.lon} is lon, and my name is {test2.name}")

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

test3 = Geocache(15, 16, "David", "hard", "big")
print(f"{test3.lat} is lat, {test3.lon} is lon, and my name is {test3.name}, {test3.difficulty} is the difficulty and the size is {test3.size}")

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint(f"Catacombs", 41.70505, -121.51521)
print(f"{waypoint.name}, {waypoint.lat}, {waypoint.lon}")

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint.__str__)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(f"{geocache.name}, diff {geocache.difficulty}, size {geocache.size}, {geocache.lon} {geocache.lat}")

# Print it--also make this print more nicely
print(geocache.__str__())

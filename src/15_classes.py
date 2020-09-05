# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class Latlon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(Latlon):
    def __init__(self, lat, lon, name):
        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        return f'{self.name}, {self.lat}, {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, diifficulty, size):
        self.difficulty = diifficulty
        self.size = size
        super().__init__(lat, lon, name)

    def __str__(self):
        return f'{self.name}, {self.lat}, {self.lon}, {self.difficulty}, {self.size}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint(41.70505, -121.51521, "Catacombs")

print(waypoint.name, waypoint.lat, waypoint.lon)




# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache(44.052137, -121.41556, "Newberry Views", "diff 1.5", "size 2")

print(geocache.lat, geocache.lon, geocache.name, geocache.difficulty, geocache.size)

# Print it--also make this print more nicely
print(geocache)

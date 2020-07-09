# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

coord = LatLon(9, 27)
print(coord.lat, coord.lon)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"

wp = Waypoint('babes', 4, 29)
print(wp.name, wp.lat, wp.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, diff, size, lat, lon):
        self.diff = diff
        self.size = size
        super().__init__(name, lat, lon)
    def __repr__(self):
        return { "name": self.name, "diff": self.diff, "size": self.size, "lat": self.lat, "lon": self.lon }
    def __str__(self):
        return f'{super().__str__()}, {self.diff}, {self.size}'
g = Geocache('mt everest', 'hard', 'big', 5, 2)
print(g.__repr__())
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)

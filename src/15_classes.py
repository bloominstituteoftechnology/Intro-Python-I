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
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return (f"{self.name}, latitude: {self.lat}, longitude: {self.lon}")


waypoint = Waypoint("House", -123, 321)

print(waypoint.name)
print(waypoint.lon)
print(waypoint.lat)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.name = name
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return (f"{self.name}, difficulty: {self.difficulty}, size: {self.size}, latitude: {self.lat}, longitude: {self.lon}")


geocache = Geocache("Half Dome", 10, 123, -123, 321)

print(geocache.name)
print(geocache.lon)
print(geocache.lat)
print(geocache.size)
print(geocache.difficulty)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

catacombs = Geocache("Catacombs", None, None, 41.70505, -121.51521)

print(catacombs.name)
print(catacombs.lat)
print(catacombs.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

newberry_views = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

print(newberry_views.name)
print(newberry_views.size)
print(newberry_views.lat)
print(newberry_views.lon)

# Print it--also make this print more nicely
print(geocache)

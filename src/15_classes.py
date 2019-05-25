# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon: 
    def __init__(self, lati, long):
        self.lat = lati
        self.lon = long
a = LatLon(13.0, 43.0)
print(a.lat, a.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon): 
    def __init__(self, name, lati, long):
        self.name = name
        super().__init__(lati, long)

    def __str__(self):
        return "Name: {}, Latitude: {}, Longitude: {}\n".format(self.name, self.lat, self.lon)

b = Waypoint("manasses", 21, 32)
print(b.lat)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache (Waypoint):
    def __init__(self, name, difficulty, size, lati, long): 
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lati, long)

    def __str__(self):
        return "Name: {}, Difficulty: {}, Size: {}, Latitude: {}, Longitude: {}\n".format(self.name, self.difficulty, self.size, self.lat, self.lon)

c = Geocache("Earth", 10.0, "enourmous", 775.3, 803.4)
print(c.name, c.lat, c.lon, c.size, c.difficulty)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.name, waypoint.lat, waypoint.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint) # BY EDITING THE CLASS ITSELF!!! Look above for str method


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)
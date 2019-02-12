# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# l = LatLon(41.70505, -121.51521)
# print(l.lat)
# print(l.lon)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    
    def __str__(self):
        return str(self.__dict__)

# w = Waypoint('Catacombs', 41.70505, -121.51521)
# print(w.name)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# inherit from Waypoint

# YOUR CODE HERE
class Geocache(Waypoint):
    # Order determines the order we pass the arguments
    def __init__(self, name, lat, lon, difficulty, size):
        # We have to call the props from the parent class
        super().__init__(name, lat, lon)
        # set our new props
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return str(self.__dict__)
        

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
w = Waypoint('Catacombs', 41.70505, -121.51521)
print(w)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
g = Geocache("Newberry Views", 44.052137, -121.41556, 1.5, 2)

# Print it--also make this print more nicely
print(g)

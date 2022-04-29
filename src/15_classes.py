# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
#  1. create a class
class LatLon:
    #  constructor, it will take in lat & lon
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
#  Because we want to inherit from LatLon then you want to pass it into the new class
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        #  because we need to pass in lat lon but its from the parent class 
        # we will use to "super class" to access the parent class
        super().__init__(lat, lon)
        self.name = name

        #  __str__ allows us to print out a more readable representation of the class
        # self is denoting that this is on the waypoint class
        # we want to return  a string
        def __str__(self):
            return f"Waypoint: {self.name}, {self.lat}, {self.lon}"


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        return f"Geocache: {self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# we call the constructor
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

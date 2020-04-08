# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# NOTE: All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created

# NOTE: The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# It does not have to be named self, you can call it whatever you like,
# but it has to be the first parameter of any function in the class:


class LatLon:
    def __init__(self, lat, lon):  # See note on self
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# NOTE: To keep the inheritance of the parent's __init__() function,
# add a call to the parent's __init__() function:


class Waypoint(LatLon):  # send the parent class as a parameter when creating the child class
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)  # see note
        self.name = name

    def __str__(self):
        return (f"{self.name} \nLatitude: {self.lat} \nLongitude: {self.lon}")

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat=0, lon=0):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return (f"{self.name} \nDifficulty: {self.difficulty} \nSize: {self.size} \nLatitude: {self.lat} \nLongitude: {self.lon}")

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 9.9, 1, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

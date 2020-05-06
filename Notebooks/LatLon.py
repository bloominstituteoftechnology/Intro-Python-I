# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon():

    def __init__(self, lat, lon):
        # Can be passed latitude and longitude.
        self.lat = lat
        self.lon = lon

    def __str__(self):
        retrin

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):

    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)  # calling on parent class
        self.name = name

    def __str__(self):
        return f'{self.name} Latitude is {self.lat} and its Longitude is {self.lon}'
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class GeoCache(Waypoint):

    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f'{self.name} Latitude is {self.lat} and, Longitude is {self.lon}. Its difficulty is {self.difficulty}, and its size is {self.size}.'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE


waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = GeoCache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache.__str__())

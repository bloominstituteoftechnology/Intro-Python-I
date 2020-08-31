# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__ (self, lat ,lon):
        self.lat = lat
        self.lon = lon

    def __str__ (self):
       return f'lat: {self.lat} lon: {self.lon}'

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__ (self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        return f'Waypoint: {self.name}, {super().__str__()}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__ (self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)
    
    def __str__(self):
        lon_lat = super().__str__()[10:]
        
        return f'Geocache: {lon_lat}, diff {self.difficulty}, size {self.size}'


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache2 = Geocache('Catacombs', 3, 4, 41.70505, -121.51521)
# YOUR CODE HERE
geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)


# Print it--also make this print more nicely
print(geocache)
print(geocache2)

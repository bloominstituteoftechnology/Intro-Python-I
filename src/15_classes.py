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


    def __repr__(self):
        return {'name': self.name, 'lat': self.lat, 'lon': self.lon}

    def __str__(self):
        print(f'Waypoint: {self.name}, {self.lat}, {self.lon}')




# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint, LatLon):
    def __init__(self, name, diff, size, lat, lon):
        super().__init__(name, lat, lon)
        self.diff = diff
        self.size = size

    def __repr__(self):
        return {'name': self.name, 'difficulty': self.diff, 'size': self.size, 'lat': self.lat, 'lon': self.lon}

    def __str__(self):
        print(f'Geocache:Name: {self.name}, Difficult: {self.diff}, size: {self.size}, lat: {self.lat}, lon: {self.lon}')



# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.__repr__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache.__repr__())

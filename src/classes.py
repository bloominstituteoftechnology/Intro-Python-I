# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class latlon:
    def __init__(self, lat=0, lon=0):
        self.lat = lat
        self.lon = lon

x = latlon(1, 22)
print(x.lat)
print(x.lon)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class waypoint(latlon):
    def __init__(self, lat, lon, name='default'):
        self.name = name
        latlon.__init__(self, lat, lon)
    def __str__(self):
        return "Name: {} Lat: {} Lon: {}".format(self.name, self.lat, self.lon)

y = waypoint(10, 11, 'test')

print(y)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class geocache(waypoint):
    def __init__(self, lat, lon, name, difficulty=1, size=0):
        self.difficulty = difficulty
        self.size = size
        waypoint.__init__(self, lat, lon, name)

z = geocache(lat=44.052137, lon=121, size=2, difficulty=1.5, name="Newberry Views")


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)

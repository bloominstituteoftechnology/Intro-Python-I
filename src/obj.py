# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

# Make a new waypoint "Catacombs", 41.70505, -121.51521
w = Waypoint("Catacombs", 41.70505, -121.51521)
# Print it

# Without changing the following line, how can you make it print into something
# more human-readable?
w = "Waypoint: name: {0}, lat: {1}, lon: {2}".format(w.name, w.lat, w.lon)

print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
g = "Geocache: name: {0}, difficulty: {1}, size: {2}, lat: {3}, lon: {4}".format(g.name, g.difficulty, g.size, g.lat, g.lon)

print(g)



#example from printf.py
#print('x is {0}, y is {1:.2f}, z is "{2}"'.format(x, y, z))
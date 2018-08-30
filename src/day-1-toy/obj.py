# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

x = LatLon(3,5);
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

y = Waypoint('place', 5, 4)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.name = name
        self.difficulty = difficulty
        self.size = size
        self.lat = lat
        self.lon = lon

# Make a new waypoint "Catacombs", 41.70505, -121.51521
w = Geocache('Catacombs', None, None, 41.70505, -121.51521)
# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print('{}, {}, {}'.format(w.name, w.lat, w.lon))

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print('{}, {}, {}, {}, {}'.format(g.name, g.difficulty, g.size, g.lat, g.lon))

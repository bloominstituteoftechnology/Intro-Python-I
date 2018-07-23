# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.


class Waypoint(LatLon):
    def __init(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


class Geocache(Waypoint, LatLon):
    def __init__(self, name, difficulty, size, lat, lon):
        self.name = name
        self.difficulty = difficulty
        self.size = size
        self.lat = lat
        self.lon = lon


# Make a new waypoint "Catacombs", 41.70505, -121.51521
Catacombs = Waypoint(41.70505, -121.51521)


# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
w = ' lat: {}, lon: {}'.format(Catacombs.lat, Catacombs.lon)
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geo = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
g = 'Name: {}, difficulty: {}, size: {}\nLat: {}, Lon: {}'.format(
    geo.name, geo.difficulty, geo.size, geo.lat, geo.lon)
print(g)

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return "Latitude:" + str(self.lat) + "\nLongitude:" + str(self.lon)
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

class Waypoint:
    def __init__(self, name, lat, lon):
        self.name = name
        self.latlon = LatLon(lat, lon)

    def __str__(self):
        return "Waypoint: " + self.name + "\n" + str(self.latlon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache:
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        self.waypoint = Waypoint(name, lat, lon)

    def __str__(self):
        return "Geocache: " + self.waypoint.name + "\nDifficulty: " + str(self.difficulty) + "\t\tSize: " + str(self.size) + "\n" + str(self.waypoint.latlon)

# Make a new waypoint "Catacombs", 41.70505, -121.51521
w = Waypoint("Catacombs", 41.70505, -121.51521)

# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(g)

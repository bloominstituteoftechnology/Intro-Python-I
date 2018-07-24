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
catacombs = Waypoint('catacombs', 41.70505, -121.51521)

# Print it
print(catacombs.name, catacombs.lat, catacombs.lon)

# Without changing the following line, how can you make it print into something
# more human-readable?
w = "\nWAYPOINT: " + str(catacombs.name) + "\nLAT: " + str(catacombs.lat) + "\nLON: " + str(catacombs.lon)
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
newberry = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
g = "\nGEOCACHE: " + str(newberry.name) + "\nDIFFICULTY: " + str(newberry.difficulty) + "\nSIZE: " + str(newberry.size) + "\nLAT: " + str(newberry.lat) + "\nLON: " + str(newberry.lon)
print(g)

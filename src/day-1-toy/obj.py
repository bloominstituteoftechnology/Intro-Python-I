# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = str(lat)
        self.lon = str(lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def printnice(self):
        return "Name: " + self.name + "\nLat: " + self.lat + "\nLon: " + self.lon

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = str(difficulty)
        self.size = str(size)
        super().__init__(name, lat, lon)

    def printnice(self):
        return "Name: " + self.name + "\nDifficulty: " + self.difficulty + "\nSize: " + self.size + "\nLat: " + self.lat + "\nLon: " + self.lon

# Make a new waypoint "Catacombs", 41.70505, -121.51521
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)
w = waypoint.printnice()
# Print it
print(waypoint)
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geo = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
g = geo.printnice()
# Print it--also make this print more nicely
print(g)

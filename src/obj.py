# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __repr__(self):
        return f"{self.__class__.__name__}({self.lat}, {self.lon})"
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        self.name = name
        super().__init__(lat, lon)
    def __repr__(self):
        return f"{self.__class__.__name__}({self.lat}, {self.lon}, {self.name})"
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty):
        self.difficulty = difficulty
        super().__init__(lat, lon, name)
    def __repr__(self):
        return f"{self.__class__.__name__}({self.lat}, {self.lon}, {self.name} {self.difficulty}) "
# Make a new waypoint "Catacombs", 41.70505, -121.51521
Catacombs = Waypoint(41.70505, -121.51521, 'Catacombs')
# Print it

print(Catacombs)
# Without changing the following line, how can you make it print into something
# more human-readable?
w = Catacombs
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache(44.052137, -121.41556, "Newberry", "diff 1.5")
# Print it--also make this print more nicely
print(g)

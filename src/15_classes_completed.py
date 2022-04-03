# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class Lation:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return str(self.__dict__)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(Lation):
    def __init__(self, name: str, lat: float, lon: float):
        super().__init__(lat, lon)
        self.name = name 

    def __str__(self):
        return str(self.__dict__)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty: float, size: float, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

y = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(y)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

z = Geocache(lat=44.052137, lon=-121.41556, size=2, difficulty=1.5, name="Newberry Views")
print(z)

# Print it--also make this print more nicely
print(Geocache)

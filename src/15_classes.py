# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat=lat, lon=lon)

    def __str__(self):
        return '{self.name} is at {self.lat} latitude and {self.lon} longitude'.format(self=self)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name=name, lat=lat, lon=lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return '{self.name} is difficulty {self.difficulty}, size {self.size} and is located at {self.lat} latitude and {self.lon} longitude'.format(self=self)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

way = Waypoint("Catacombs", 41.70505, -121.51521)
print(way.name, way.lat, way.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(way)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

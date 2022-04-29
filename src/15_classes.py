# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed
# parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.


class waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


class Geocache(waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return "{self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}".format(self=self)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
class waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return "{self.name}, {self.lat}, {self.lon}".format(self=self)

waypoint = waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geo = Geocache(44.052137, -121.41556, name="Newberry Views",
               difficulty='diff 1.5', size='size 2')

# Print it--also make this print more nicely
# print(geocache)
print(geo)

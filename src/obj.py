# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon(object):
    def __init__(self, lat, lon):
        self.lat = lat,
        self.lon = lon,
        super().__init__()

    def __str__(self):
        return """LatLon(
            {self.lat}
            {self.lon})""".format(self=self)


# Make a class Waypoint that can be passed parameters
# `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name,
        super(Waypoint, self).__init__(lat, lon)

    def __str__(self):
        return """Waypoint(
            {self.name}
            {self.lat}
            {self.lon})""".format(self=self)


# Make a class Geocache that can be passed parameters
# `name`, `difficulty`, `size`, `lat`, and `lon` to the constructor.
# What should it inherit from?
class Geocache(Waypoint, LatLon):
    def __init__(self, difficulty, size, name, lat, lon):
        self.difficulty = difficulty,
        self.size = size,
        super().__init__(name, lat, lon)

    def __str__(self):
        return """Geocache(
            {self.difficulty}
            {self.size}
            {self.name}
            {self.lat}
            {self.lon})""".format(self=self)


# Make a new waypoint "Catacombs", 41.70505, -121.51521
w = Waypoint(41.70505, -121.51521, 'Catacombs')

# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache('NewBerry Views', 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(g)

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return """
{0}:
lat {1}
lon {2}
""".format(self.__class__.__name__, w.lat, w.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.


class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return super().__str__() + """\
name {}
""".format(w.name)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return super().__str__() + """\
difficulty {}
size {}
""".format(g.difficulty, g.size)


# Make a new waypoint "Catacombs", 41.70505, -121.51521
w = Waypoint(41.70505, -121.51521, "Catacombs")

# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)

# Print it--also make this print more nicely
print(g)

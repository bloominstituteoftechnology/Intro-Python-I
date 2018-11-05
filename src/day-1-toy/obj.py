# referenced here https://docs.python.org/3/tutorial/classes.html
# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.


class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# Make a new waypoint "Catacombs", 41.70505, -121.51521


# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# Print it--also make this print more nicely
print(g)

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat=0, lon=0):
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return "-Lat:{} -Lon:{}".format(self.lat, self.lon)
    
    def __str__(self):
        return "-Lat:{} -Lon:{}".format(self.lat, self.lon)
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

class Waypoint(LatLon):
    def __init__(self, name="", lat=0, lon=0):
        self.name = name
        self.latlon = LatLon(lat, lon)
        # self.lat = lat
        # self.lon = lon

    def __repr__(self):
        return "Name:{} {}".format(self.name, self.latlon)

    def __str__(self):
        return "Name:{} {}".format(self.name, self.latlon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, name="", diff=0, size=0, lat=0, lon = 0):
        # self.name = name
        self.waypoint = Waypoint(name, lat, lon)
        self.diff = diff
        self.size = size
        # self.lat = lat
        # self.lon = lon

    def __repr__(self):
        return "{} -Diff:{} -Size:{}".format(self.waypoint, self.diff, self.size)

    def __str__(self):
        return "{} -Diff:{} -Size:{}".format(self.waypoint, self.diff, self.size)

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
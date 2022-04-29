# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    lat = 0
    lon = 0

    def __init__(self, lat, lon):
        self.lat = lat;
        self.lon = lon;


location = LatLon(10, 424)
print(location.lat)
print(location.lon)


# # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# # constructor. It should inherit from LatLon. Look up the `super` method.
#
class Waypoint(LatLon):
    name = ""

    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return self.name + ',' + str(self.lat) + ',' + str(self.lon)


waypoint = Waypoint("Nick", 232, 42)
print(waypoint.name)


#
# # Make a class Geocache that can be passed parameters `name`, `difficulty`,
# # `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# Inherit from Waypoint

class Geocache(Waypoint):
    difficulty = ""
    size = ""

    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return '' + self.name + ',' + str(self.difficulty) + ',' + str(self.size) + ',' + str(self.lat) + ',' + str(
            self.lon) + ''


geocache = Geocache("Nick", "super", 234, 123213, 123)
print(geocache.difficulty)
# # Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
newWaypoint = Waypoint("Catacombs", 41.70505, -121.51521)

#
# # Without changing the following line, how can you make it print into something
# # more human-readable? Hint: Look up the `object.__str__` method
print(newWaypoint)
#
# # Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
newGeocache = Geocache("Newberry", "diff 1.5", "size 2", 44.052137, -121.41556)
print(newGeocache)

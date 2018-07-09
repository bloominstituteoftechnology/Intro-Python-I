# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
            # return("blabla  pi%s%s%s".format(self.name, self.lat, self.lon))
            return f'name: {self.name}, lat: {self.lat}, lon: {self.lon}'
            # return("%s%s%s".format(self.name, self.lat, self.lon))


# # Make a class Geocache that can be passed parameters `name`, `difficulty`,
# # `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, difficulty, size, name, lat, lon ):
        super().__init__(name, lat, lon)
        self.size = size
        self.difficulty = difficulty

    def __str__(self):
            # return("blabla  pi%s%s%s".format(self.name, self.lat, self.lon))
            return f'name: {self.name}, difficulty: {self.difficulty}, size: {self.size},  lat: {self.lat}, lon: {self.lon}'
            # return("%s%s%s".format(self.name, self.lat, self.lon))

# # Make a new waypoint "Catacombs", 41.70505, -121.51521
w = Waypoint('Catacombs', 41.70505, - 121.51521)
# # Print it
# #
# # Without changing the following line, how can you make it print into something
# # more human-readable?
print(w)

# # Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache(1.5, 2,"Newberry Views", 44.052137, -121.41556)

# # Print it--also make this print more nicely
print(g)

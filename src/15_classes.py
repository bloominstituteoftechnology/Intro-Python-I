# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

latLon = LatLon(lat=5, lon=6)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self,
                name,
                lat,
                lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return"{}: \n\tcoords = {}, {}\n".format(self.name,
                                        self.lat,
                                        self.lon)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self,
                name,
                difficulty,
                size,
                lat,
                lon):
        super().__init__(name=name, lat=lat, lon=lon)
        self.difficulty = difficulty
        self.size = size    
    def __str__(self):
        return "{}:\n\tdifficulty = {}\n\tsize = {}\n\tcoords = {}, {}\n".format(
            self.name,
            self.difficulty,
            self.size,
            self.lat,
            self.lon
        )
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(name="Catacombs", lat=41.70505,lon=-121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(
    "Newbery Views",
     1.5,
     2,
     44.052137,
     -121.41557
)
# Print it--also make this print more nicely
print(geocache)

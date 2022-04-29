# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.lat, self.lon)


loc_1 = Waypoint("New York", 10, 10)
print(loc_1)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.name, self.difficulty, self.size, self.lat, self.lon)


loc_3 = Geocache("Everest", "Hard", 10000, 10, 50)
print(loc_3)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
loc_4 = Waypoint("Catacombs", 41.70505, -121.51521)
print(loc_4)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
geocache = Geocache("Newberry Views", "diff 1.5",
                    "size 2", 44.052137, -121.41556)
print(geocache)

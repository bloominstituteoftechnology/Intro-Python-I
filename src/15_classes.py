# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super(Waypoint, self).__init__(lat, lon)
    def __str__(self):
        return f"Name: {self.name}, Coordinates: {self.lat} lattitude and {self.lon} longitude"

# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super(Geocache, self).__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

        def __str__(self):
            return f"Name: {self.name}, Coordinates: {self.lat} lattitude and {self.lon} longitude, Difficulty: {self.difficulty}, Size: {self.size}"

# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print(Waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)

# Print it--also make this print more nicely
print(Geocache)

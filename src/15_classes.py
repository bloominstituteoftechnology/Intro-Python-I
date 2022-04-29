# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

place1 = LatLon(130,-130)

print(place1.lat, place1.lon)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class waypoint(LatLon):
  def __init__(self, lat, lon, name):
    super(waypoint, self).__init__(lat, lon)
    self.name = name
  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}"



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(waypoint):
  def __init__(self, lat, lon, name, difficulty, size):
    super(Geocache, self).__init__(lat, lon, name)
    self.difficulty = difficulty
    self.size = size
  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}, {self.difficulty}, {self.size}."

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
Waypoint = waypoint(41.70505,-121.51521, "Catacombs")

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(Waypoint)

# Make a new geocache "c", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137,-121.41556, "c", "diff 1.5", "size 2")
# Print it--also make this print more nicely
print(geocache)


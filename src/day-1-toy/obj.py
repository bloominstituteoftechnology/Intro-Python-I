# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon():
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
  def __init__(self, name, lat, lon):
    super().__init__(lat, lon)
    self.name = name
    # return "The {} is at lat:{} and lon:{}".format(name,lat,lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class GeoCache(Waypoint):
  def __init__(self, name, difficulty, size, lat, lon):
    super().__init__(name, lat, lon)
    self.difficulty = difficulty
    self.size = size


# Make a new waypoint "Catacombs", 41.70505, -121.51521

# w = Waypoint(name="Catacombs", lat=41.70505, lon=-121.51521)
w = Waypoint('Catacombs', 41.70505, -121.51521)
print(w.name)
print(w.lat)
print(w.lon)
# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = GeoCache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(g.name)
print(g.difficulty)
print(g.size)
print(g.lat)
print(g.lon)
# Print it--also make this print more nicely
print(g)

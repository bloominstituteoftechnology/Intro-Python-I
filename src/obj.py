# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
  def __init__(lat, lon):
    self.lat = lat
    self.lon = lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
  def __init__(name, lat, lon):
    self.name = name
    self.lat = LatLin.lat
    self.lon = LatLin.lon

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(LatLon, Waypoint):
  def __init__(name, difficulty, size, lat, lon):
    self.name = name
    self.difficulty = difficulty
    self.size = size
    self.lat = Waypoint.lat
    self.lon = Waypoint.lon
# Make a new waypoint "Catacombs", 41.70505, -121.51521
    w = Waypoint("catacomb", "41.75505", "-121.51521")
# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
    print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# Print it--also make this print more nicely
    print(g)

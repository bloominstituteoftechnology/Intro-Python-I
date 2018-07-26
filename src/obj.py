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
    self.name = name
    LatLon.__init__(self, lat, lon)
  def __str__(self):
    return "Waypoint: name=\"%s\" lat=%s lon=%s" % (self.name, self.lat, self.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
  def __init__(self, name, difficulty, size, lat, lon):
    self.size = size
    self.difficulty = difficulty
    Waypoint.__init__(self, name, lat, lon)
  def __str__(self):
    return "Geocache: name=\"%s\" difficulty=%s size=%s lat=%s lon=%s" % (self.name, self.difficulty, self.size, self.lat, self.lon)


# Make a new waypoint "Catacombs", 41.70505, -121.51521

new_waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Print it

print(new_waypoint)

# new_geocache = Geocache("NEWGEO", "Hard", "BIG", 10, 40.5)
# print(new_geocache)

# Without changing the following line, how can you make it print into something
# more human-readable?
w = str(new_waypoint)
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(g)

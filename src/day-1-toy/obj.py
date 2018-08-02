# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
  
  def __str__(self):
    return f'The latitude is {self.lat} and longitude is {self.lon}'


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
  def __init__(self, name, lat, lon):
    LatLon.__init__(self, lat, lon)
    self.name = name
  
  def __str__(self):
    return f'Waypoint name: {self.name}, latitude is {self.lat} and longitude is {self.lon}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
  def __init__(self, name, difficulty, size, lat, lon):
    Waypoint.__init__(self, name, lat, lon)
    self.difficulty = difficulty
    self.size = size

  def __str__(self):
    return f'Geocache location: {self.name}, difficulty: {self.difficulty}, size: {self.size}, latitude: {self.lat}, longitude: {self.lon}'

# Make a new waypoint "Catacombs", 41.70505, -121.51521
w = Waypoint('Catacombs', 41.70505, -121.51521)
# Print it
print(w)

# Without changing the following line, how can you make it print into something
# more human-readable?
ll = LatLon(41.70505, -121.51521)
print(ll)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(g)

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
  lat = 0
  lon = 0

  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

  def getLat(self):
    return self.lat

  def getLon(self):
    return self.lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
  name = ""

  def __init__(self, name, lat, lon):
    self.name = name

    super().__init__(lat, lon)

  def __repr__(self):
    return { 'name':self.name, 'lat':self.lat, 'lon':self.lon }

  def __str__(self):
    return f"{self.name} {self.lat} {self.lon}"

  def getName(self):
    return self.name

  def getWaypoint(self):
    return f"{self.name} {self.lat} {self.lon}"



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
  diff = ""
  size = ""

  def __init__(self, name, diff, size, lat, lon):
    self.diff = diff
    self.size = size

    super().__init__(name, lat, lon)

  def __str__(self):
    return f"'{self.name}' Difficulty: {self.diff} Size: {self.size} Coords: {self.lat}, {self.lon}"

  def getDifficulty(self):
    return self.diff

  def getSize(self):
    return self.size

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint.getWaypoint())

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

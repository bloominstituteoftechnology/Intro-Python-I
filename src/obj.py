# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon():
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

testing = LatLon(222.22, 3333.333)
print(testing.lat)
  
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
  def __init__(self, lat, lon, name):
    super().__init__(lat, lon)
    self.name = name

test = Waypoint(1.111, 4.534343, "Test")
print(test.name)
print(test.lat)
print(test.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# Make a new waypoint "Catacombs", 41.70505, -121.51521

class Geocache(Waypoint):
  def __init__(self, name, difficulty, size, lat, lon):
    super().__init__(lat, lon, name)
    self.difficulty = difficulty
    self.size = size

test3 = Geocache("Test 3", "Hard", 4.5, 4.3232, 7.7777)
print(test3.name)
print(test3.difficulty)
print(test3.size)
print(test3.lat)
print(test3.lon)

# print("%i %.2f %s" %(x, y, z))
w = "Name: %s Difficulty: %s Size: %f Lat: %f Lon: %f" %(test3.name, test3.difficulty, test3.size, test3.lat, test3.lon)

# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
test4 = Geocache("Newberry Views", "1.5", 2, 44.052137, -121.41556)
g = "Name: %s Difficulty: %s Size: %f Lat: %f Lon: %f" %(test4.name, test4.difficulty, test4.size, test4.lat, test4.lon)
# Print it--also make this print more nicely
print(g)


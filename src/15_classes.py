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
class WayPoint(LatLon):

	def __init__(self, lat, lon, name):
		LatLon.__init__(self, lat, lon)
		self.name = name

	def __str__(self):
		return "\nlocation: {}".format(self.name) + " " + "\nlatitude: {}".format(self.lat) + " " + "\nlongitude: {}".format(self.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(LatLon):

	def __init__(self, lat, lon, name, difficulty, size):
		LatLon.__init__(self, lat, lon)
		self.name = name
		self.difficulty = difficulty
		self.size = size

	def __str__(self):
		return (
			"\nlocation: {}".format(self.name) + \
			"\ndifficulty: {}".format(self.difficulty) + \
			"\nsize: {}".format(self.size) + \
			"\nlatitude: {}".format(self.lat) + \
			"\nlongitude: {}".format(self.lon)
		)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
waypoint_location = WayPoint(41.70505, -121.51521, "Catacombs")
# print(waypoint_location.lat, waypoint_location.lon, waypoint_location.name)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print(waypoint_location)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache_location = Geocache(44.052137, -121.41556, "Newberry Views", "diff 1.5", "size 2")


# Print it--also make this print more nicely
print(geocache_location)

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
	def __init__(self, lat=0, lon=0):
		self.lat = lat
		self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):	
	def __init__(self, name, lat=0, lon=0):
		super().__init__(lat, lon)
		self.name = name
	
	def __repr__(self):
		return "<Waypoint {}: {:f}, {:f}>".format(self.name, self.lat, self.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
	def __init__(self, name, difficulty, size, lat=0, lon=0):
		super().__init__(name, lat, lon)
		self.difficulty = difficulty
		self.size = size
	
	def __repr__(self):
		return f"<Geocache '{self.name}, {self.difficulty} {self.size} {self.lat:f}, {self.lon:f}'>"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

catacombs = Waypoint("Catacombs", 41.70505, -121.51521)
print(catacombs)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

waypoint = "Waypoint {} at Latitude {} and Longitude {}".format(catacombs.name, catacombs.lat, catacombs.lon)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

newberry_views = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely

geocache = "Waypoint {} at Latitude {} and Longitude {} with a difficulty of {} and size {}".format(newberry_views.name, newberry_views.lat, newberry_views.lon, newberry_views.difficulty, newberry_views.size)
print(geocache)



place = LatLon(17.9000, 62.8333)

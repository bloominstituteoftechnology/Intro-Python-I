# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:

	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)
    
  # def __repr__(self):
  #   return f'Latitude {self.lat} and Longitude {self.lon}'

  # def __repr__(self):
	# 	return str(self.__class__) + ": " + str(self.__dict__)

place = LatLon(17.9000, 62.8333)
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):	
	def __init__(self, name, lat, lon):
		super().__init__(lat, lon)
		self.name = name

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
	def __init__(self, name, difficulty, size, lat, lon):
		super(Geocache, self).__init__(name, lat, lon)
		self.difficulty = difficulty
		self.size = size
  
  # def getField(self, name, default=None):
  #   "Return field's value as a string (even if it's an uploaded file)"
  #   pass

  # def __repr__(self):
  #   return f'Latitude {self.lat} and Longitude {self.lon}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

catacombs = Waypoint("Catacombs", 41.70505, -121.51521)
print(catacombs)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

waypoint = "{} at Latitude {} and Longitude {}".format(catacombs.name, catacombs.lat, catacombs.lon)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

newberry_views = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely

geocache = "{} at Latitude {} and Longitude {} with a difficulty of {} and size {}".format(newberry_views.name, newberry_views.lat, newberry_views.lon, newberry_views.difficulty, newberry_views.size)
print(geocache)


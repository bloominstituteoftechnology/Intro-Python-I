class LatLon:

	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon

class WayPoint(LatLon):

	def __init__(self, lat, lon, name):
		LatLon.__init__(self, lat, lon)
		self.name = name


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


location_1 = LatLon(125, -456)
waypoint_location = WayPoint(125, -456, "Las Vegas")

print(location_1.lat, location_1.lon)
print()
print(waypoint_location.lat, waypoint_location.lon, waypoint_location.name)


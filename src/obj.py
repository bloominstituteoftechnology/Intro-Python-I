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
        super().__init__(lat, lon)
        self.name = name
    
   



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class GeoCache(Waypoint):
    def __init__(self, difficulty, size, name, lat, lon):
        super().__init__(name, lat, lon)
        self.size = size
        self.difficulty = difficulty
        
# Make a new waypoint "Catacombs", 41.70505, -121.51521

new_waypoint = Waypoint('catacombs', 41.70505, -121.51521)
print(new_waypoint.name, new_waypoint.lat, new_waypoint.lon)
# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
w = "Name: " + str(new_waypoint.name) + "\n" + "Latitude: " + str(new_waypoint.lat) + "\n" + "Longitude: " + str(new_waypoint.lon)
print(w)

geo = GeoCache("Newberry Views", "diff 1.5", "size 2", 44.052137, -121.41556)
print(geo.name)
g = "Name: {0}\nDifficulty: {1}\nSize: {2}\nLat: {3}\nLon: {4}\n".format(geo.name, geo.difficulty, geo.size, geo.lat, geo.lon)
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556


# Print it--also make this print more nicely
print(g)

# also defining a function inside the classes might be a better solution.

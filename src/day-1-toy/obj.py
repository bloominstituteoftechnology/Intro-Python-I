# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super(Waypoint,self).__init__(lat, lon)
    def __repr__(self):
        return f"name: {self.name}, lat: {self.lat}, lon: {self.lon}"
        
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super(Geocache,self).__init__(name, lat, lon)
    def __repr__(self):
        return f"name: {self.name}, lat: {self.lat}, lon: {self.lon}, difficulty: {self.difficulty}, size: {self.size}"

# Make a new waypoint "Catacombs", 41.70505, -121.51521

a = Waypoint('Catacombs', 41.70505, -121.51521)
# addition.name('Catacombs')
# addition.lat('41.70505')
# addition.lon('-121.51521')


# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# Print it--also make this print more nicely
print(g)

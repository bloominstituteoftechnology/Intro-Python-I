# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon():
        def __init__(self, lat,lon):
                self.lat=lat
                self.lon=lon




# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
        def __init__(self,name,lat,lon):
                self.name=name
                super().__init__(lat,lon)

        def __str__(self):
                return f'name: {self.name}, lat: {self.lat}, lon: {self.lon}'

w=Waypoint("Catacombs", 41.70505, -121.51521)                
                
print(w)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
        def __init__(self, name, difficulty, size, lat, lon):
                super().__init__(name,lat,lon)
                self.size=size
                self.difficulty=difficulty
        def __str__(self):
                return f'name: {self.name}, lat: {self.lat}, lon: {self.lon}, size: {self.size} difficulty: {self.difficulty}'    
                
g = Geocache("Newberry Views",1.5, 2, 44.052137, -121.41556)
print(g)


# Make a new waypoint "Catacombs", 41.70505, -121.51521

# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# Print it--also make this print more nicely

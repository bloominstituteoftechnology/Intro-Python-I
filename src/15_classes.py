# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return 'Waypoint(name='+self.name+', lat='+str(self.lat)+ ', lon='+str(self.lon) +')'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return 'Geocache(\nname '+self.name+',\n difficulty '+str(self.difficulty)+',\n size '+str(self.size)+',\n lat '+str(self.lat)+',\n lon '+str(self.lon)+')'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
Waypoint_1 = Waypoint('Catacombs', 41.70505, -121.51521)
print(Waypoint_1)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geo_1 = Geocache(name = "Newberry Views", difficulty = 1.5, size = 2, lat = 44.052137, lon = -121.41556)

# Print it--also make this print more nicely
print(geo_1)

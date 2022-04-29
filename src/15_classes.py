# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat=lat
        self.lon=lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, **kwds):
        self.name=name
        super().__init__(**kwds)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# It should inherit from Waypoint
class Geocache(Waypoint):
    def __init__(self, difficulty, size, **kwds):
        self.difficulty=difficulty
        self.size=size
        super().__init__(**kwds)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(name="Catacombs", lat=41.70505, lon=-121.51521)
print(f'"{waypoint.name}", {waypoint.lat}, {waypoint.lon}')

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

# Add the method __str__ to the Waypoint class
class Waypoint(LatLon):
    def __init__(self, name, **kwds):
        self.name=name
        super().__init__(**kwds)
    
    def __str__(self):
        return 'Waypoint(name='+self.name+', lat='+str(self.lat)+', lon='+str(self.lon)+')'
waypoint = Waypoint(name="Catacombs", lat=41.70505, lon=-121.51521)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

class Geocache(Waypoint):
    def __init__(self, difficulty, size, **kwds):
        self.difficulty=difficulty
        self.size=size
        super().__init__(**kwds)
    
    def __str__(self):
        return 'Geocache(name='+self.name+', diff='+str(self.difficulty)+', size='+str(self.size)+ \
            ', lat='+str(self.lat)+', lon='+str(self.lon)+')'

geocache = Geocache(name="Newberry Views", difficulty=1.5, size=2, lat=44.052137, lon=-121.41556)

# Print it--also make this print more nicely
print(geocache)

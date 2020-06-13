# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    
    def __init__(self, latitude = 0, longitude = 0)
        self.lat = latitude
        self.lon = longitude

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    
    def __init__(self, name, lat, lon)
        self.name = name
        super().__init__(lat, lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocode:
    
    def __init__(self, name, difficulty, size, lat, lon)
        self.name = name
        self.difficulty = difficulty
        self.size = size(filename)
        
        

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)

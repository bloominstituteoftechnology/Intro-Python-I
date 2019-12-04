# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# can inherit from more than one parent class 
# self: we can access attri
# YOUR CODE HERE

# two __ on each side of init or type error 

class LatLon(): #do i need params here?
    '''Not manadtory but adding a docString anyway'''
    def __init__(self, lat,lon): #constructor
        self.lat = lat #seld sets attribute to name 
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    def __init__(self,name,lat, lon): #missing attributes give type error expected position err
        super().__init__(lat, lon)
        self.name = name
          
    def __str__(self):
        return f'Ncame: {self.name}, Lat:{self.lat}, Lon:{self.lon}'
# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, difficulty, size, name, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
        
    def __str__(self):
        return f'Name: {self.name}, Diff:{self.difficulty}, Size:{self.size}, Lat:{self.lat}, Lon:{self.lon}'
        
# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

print(waypoint)
# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)

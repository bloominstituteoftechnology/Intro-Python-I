# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
#how do i create a class
#how do i create a class that can be passed parameters - i think with _init_ function
class LatLon:
    def __init__(self, lat, lon):
        
        self.lat = lat
        self.lon = lon
        print(lat, 'is latitude', lon, 'is longitude')

example = LatLon(22, 22)
print(example.lat)




# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
#do I still need lat and lon or are they inherited?
#how does super method work -- it calls the init function of the superclass
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return '{self.name}, {self.lat}, {self.lon}'.format(self=self)



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return '{self.name}, {self.difficulty}, {self.size}, {self.lat}, {self.lon}'.format(self=self)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint('Catacombs', 41.70505, -121.51521 )
# YOUR CODE HERE
print(waypoint)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)

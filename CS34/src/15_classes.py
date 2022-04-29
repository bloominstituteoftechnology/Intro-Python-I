# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE

class LatLon():
    def __init__(self,lat, lon):
        self.lat = lat
        self.lon = lon
thing1 = LatLon(23,35)        

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
names = Waypoint(12, 543, "Detroit")
print(str(names.lat))
print(str(names.lon))
print(str(names))



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, lat, lon, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size  = size

        #def __repr__(self):
        #return {'name':self.name, 'lat':self.lat, 'lon':self.lon}
loca = Geocache(12, 543, "Detroit", "hard", 10)
print(str(loca.difficulty))
print(str(loca.size))


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint(41.70505, -121.51521,"catacombs")
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint.__str__())
print(waypoint.__repr__())

    

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(41.5, 44.052137,"Newberry Views" ,difficulty = "hard", size = 2)
# Print it--also make this print more nicely
print(geocache)
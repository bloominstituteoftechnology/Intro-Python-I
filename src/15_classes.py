# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon



Cordin = LatLon(120,120)

print(f"lat: {Cordin.lat}")
print(f"lon: {Cordin.lon}")

# YOUR CODE HERE

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self,name,lat,lon):
        super().__init__(lat,lon)
        self.name = name
    
    def __str__(self):
        return 'This is {self.name} lat: {self.lat} lon: {self.lon}'.format(self=self)

# YOUR CODE HERE

missing = Waypoint("joshua", 120,188)
print(f"this is {missing.name}'s lat: {missing.lat} lon:{missing.lon}.  good luck")

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?


class Geocache(Waypoint):
    def __init__(self,name,difficulty,size,lat,lon):
        super().__init__(name,lat,lon)
        self.difficulty = difficulty
        self.size = size

# YOUR CODE HERE

details = Geocache("dani",10,"small",200, 200)
print(f"this is {details.name} lat: {details.lat} lon: {details.lon}, size: {details.size}, difficulty: {details.difficulty}")

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

NewWay = Waypoint("Catacombs", 41.70505,-121.51521 )
print(NewWay)

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(NewWay)


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

NewGeo = Geocache("Newberry Views",1.5, 2, 44.052137, -121.41556)
print(NewGeo)
# YOUR CODE HERE

# Print it--also make this print more nicely
# print(Geocache)

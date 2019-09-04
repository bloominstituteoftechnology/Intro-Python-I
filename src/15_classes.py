# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat=lat
        self.lon=lon
    def printlatlon(self):
        print(f"my lat lon are: {self.lat} and + { self.lon}")
    
    


p1=LatLon(5,6)
p1.printlatlon()
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
  def __init__(self, lat, lon, name):
    super().__init__(lat, lon)
    self.name = name

p1=Waypoint(5, 6, "name of location")
print(p1.name)


# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty=difficulty
        self.size=size

p2=Geocache(5,7, "name", "hard", "small")
print(p2.size)

# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
new_wave=Waypoint( 41.70505, -121.51521, "Catacombs")
print(f"{new_wave.name}, {new_wave.lat}, {new_wave.lon}")
print(new_wave.__str__())
print("hello")

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

new_geo=Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)
print(f"{new_geo.name}, diff {new_geo.difficulty}, size {new_geo.size}, {new_geo.lat}, {new_geo.lon} ")
# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)

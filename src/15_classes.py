# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat , lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

    def Waypoint(self, name):
        self.name = name
        print(f"New Waypoint is {name}, {self.lat} {self.lon}")
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

    def Geocache(self , difficulty, size):
        self.difficulty = difficulty
        self.size = size
        return f"The Waypoint {self.name} has difficulty of {self.difficulty}, size: {self.size} with Longitude: {self.lon} and Latitude: {self.lat}"

    def __str__(self):
            return f"Way point name is: {self.name}"
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = LatLon(41.70505 , -121.51521)
waypoint.Waypoint( "Catacombs")


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
    
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = LatLon(44.052137 , -121.41556)
geocache.Waypoint("Newberry Views")
print(geocache.Geocache(1.5, 2))

# Print it--also make this print more nicely
print(geocache)

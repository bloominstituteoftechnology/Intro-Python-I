# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# Making the class LatLon
class LatLon:

    def __init__(self, lat, lon):
        self.lon = lon
        self.lat = lat

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# Making the class Waypoint
class Waypoint(LatLon):

    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    # adding the __str__ method for the
    # class of Waypoint
    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# Making the class Geocache
class Geocache(Waypoint):
    
    def __init__(self, name , difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    # the __str__ method for the geocache class
    def __str__(self):
        return f"{self.name}, diff {self.difficulty}, size {self.size}, {self.lat}, {self.lon}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# making the new waypoint
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

print(waypoint.name, waypoint.lat, waypoint.lon)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# making the geochace object
geo = Geocache("Newberry Views", difficulty=1.5, size=2,
                lat= 44.052137, lon=-121.41556)

# Print it--also make this print more nicely
print(geo)

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
san_francisco = LatLon(37, 122)
print("Latitude: %s, Longitude: %s" %(str(san_francisco.lat), str(san_francisco.lon)))

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint (LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        return "Name: %s, Latitude: %s, Longitude: %s" %(self.name, self.lat, self.lon)
some_waypoint = Waypoint("My Waypoint", 37, 122)
print("Name: %s, Latitude: %s, Longitude: %s" %(some_waypoint.name, str(some_waypoint.lat), str(some_waypoint.lon)))
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache (Waypoint):
    def __init__(self, difficulty, size, name, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __str__(self):
        return "Name: %s, Difficulty: %s, Size: %s Latitude: %s, Longitude: %s" %(self.name, self.difficulty, self.size, self.lat, self.lon)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
new_waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)
print(str(new_waypoint))
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
new_geocache = Geocache(1.5, 2, "Newberry Views", 44.052137, -121.41556)
# Print it--also make this print more nicely

print(str(new_geocache))
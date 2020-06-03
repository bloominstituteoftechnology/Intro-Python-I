# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

test = LatLon(22,33)
print(test.lat, test.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        self.name = name

        super().__init__(lat, lon)

    def __str__(self):
        return 'Waypoint(name: ' + self.name + ', lat: ' + str(self.lat) + 'lon: ' + str(self.lon)+')'

test_Waypoint = Waypoint(33, 22, "John")
print(test_Waypoint.name)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        self.difficulty =  difficulty
        self.size = size

        super().__init__(lat, lon, name)
    def __str__(self):
        return 'Geocache(name:' + self.name + ', lat: ' + str(self.lat) + ', lon: ' + str(self.lon) + ', size: ' + str(self.size) + ', difficulty: ' + str(self.difficulty)
# test_Geocache = Geocache(11,22,"John", "good", "heavy")
# print(test_Geocache.difficulty, test_Geocache.size)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", "diff 1.5", "size 2")
# Print it--also make this print more nicely
print(geocache)

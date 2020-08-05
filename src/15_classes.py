# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# YOUR CODE HERE

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def printstuff(self):
        print(self.name, self.lat, self.lon)
        # print(self.lat, self.lon, self.name)

    def __str__(self):
        return 'name: {self.name}, lat: {self.lat}, lon: {self.lon}'.format(self=self)


# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, size, difficulty, name, lat, lon):
        super().__init__(name, lat, lon)
        self.size = size
        self.difficulty = difficulty

    def __str__(self):
        return 'name: {self.name}, lat: {self.lat}, lon: {self.lon}, difficulty: {self.difficulty}, size: {self.size}'.format(self=self)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint1 = Waypoint("Catacombs", 41.70505, -121.51521)
waypoint1.printstuff()
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
        #print(waypoint)
print(waypoint1)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache(2, 1.5, "Newberry Views", 44.052137, -121.41556)
# YOUR CODE HERE
print(geocache)
# Print it--also make this print more nicely
        #print(geocache)

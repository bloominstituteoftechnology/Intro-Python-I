# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def _init_(self, lat, lon):
        self.lat = lat
        self.lon = lon

        def _str_(self):
            return f"lat: {self.lat}, lon: {self.lon}"

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def _init_(self, name, lat, lon):
        self.name = name
        super()._init_(lat, lon)  # This lines prevents us from building another initializer for the same class LatLon. We're just calling the method from LatLon and saving some time by doing so.

# This is the string representation I would like to use when printing this information:
    def __str__(self):
        return f"Waypoint: {self.name}, {self.lat}, {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def _init_(self, name, diff, size, lat, lon):
        self.diff = diff
        self.size = size
        super()._init_(name, lat, lon)  # This line is inheriting from Waypoint, and we're just adding an extra parameter "Difficulty" and " Size" to it.

# This is the string representation I would like to use when printing this information:
    def __str__(self):
        return f"Geocache: Name: {self.name}, Latitude: {self.lat}, Longitude: {self.lon}, diff: {self.diff}, size: {self.size}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

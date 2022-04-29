# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f'lat: {self.lat} \n lon: {self.lon}'
# latlon = LatLon("1", "2")
# print(latlon, '\n')

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return super().__str__() + f'\n name: {self.name}'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, difficulty, size, name, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return super().__str__() + f'\n difficulty: {self.difficulty} \n size: {self.size}'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE

new_waypoint = Waypoint("Catacombs", "-41.70505", "-121.51521")
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print('\n', new_waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE

geocache = Geocache("1.5", "2", "Newberry Views", "44.052137", "-121.41556")

# Print it--also make this print more nicely
print('\n', geocache)
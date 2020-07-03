# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


l = LatLon(14, -120)
print(l.long)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, lat, long, name):
        self.name = name
        super().__init__(lat, long)

    def __str__(self):
        return f'name:{self.name}, latitude: {self.lat}, longitude: {self.long}'


l2 = Waypoint(1, 2, 'place')
print(l2.name)

# Make a class Geocache that can be passed parameters: `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, long):
        self.difficulty = difficulty
        self.size = size
        super().__init__(lat, long, name)

    def __str__(self):
        current = f'difficulty: {self.difficulty}, size: {self.size}'
        appended = Waypoint.__str__(self)
        return current+appended


geocache = Geocache('new_place', 'hard', 'big', 90, 77)
print(geocache.name, geocache.difficulty,
      geocache.lat, geocache.long, geocache.size)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
print(waypoint.name, waypoint.lat, waypoint.long)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)

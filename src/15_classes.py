# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
# self is "this" in js


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        print(f'I am {lat}, I am {lon}')


# test = LatLon(20, 40)
# print(test)


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# super() will allow to inherit everything from parent class that is passed in

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name


# print(Waypoint)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

# class Geocache(Waypoint):
#     def __init__(self, name, difficulty, size, lat, lon):
#         super().__init__(name, difficulty, size, lat, lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
new = Waypoint("Catacombs", 41, -121)
print(new)


# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)

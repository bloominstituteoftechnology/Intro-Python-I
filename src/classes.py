# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


import pprint


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
        # constructor. It should inherit from LatLon. Look up the `super` method.

        # YOUR CODE HERE


lat_1 = LatLon(100, 50)
print("Lat:", lat_1.lat)


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])


way_1 = Waypoint("Medellin", 200, 101)
print("Name:", way_1.name, way_1.lat)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, difficulty, size, name, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE


new_waypoint = Geocache("Moderate", "Large", "Catacombs", 41.70505, -121.51521)
print("Answer: ", new_waypoint.difficulty)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
waypoint = Waypoint("London", 2, 1)
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache(1.5, 2, "Newberry Views", 44.052137, 121.41556)
print(geocache.name)

# Print it--also make this print more nicely


pprint.pprint(geocache.name)

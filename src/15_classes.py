# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    lat = 0
    lon = 0
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lon = longitude


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    name = ""
    def __init__(self, wp_latitude, wp_longitude,  wp_name):
        LatLon.__init__(self, wp_latitude, wp_longitude)
        self.name = wp_name
    def __str__(self):
        return 'waypoint' + str(self.name) + ',' + str(self.wp_latitude) + ',' + str(self.wp_longitude) + '.' 

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?



# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
latLon = LatLon(41.70505, -121.51521)
waypoint = Waypoint('Catacombs', 41.70505, -121.5152)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        pass



# # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# # constructor. It should inherit from LatLon.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    
    def __str__(self):
        return "Cache %s is located at %.5f latitude, %.5f longitude" % (self.name, self.lat, self.lon)


    
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# # `size`, `lat`, and `lon` to the constructor. Wphat should it inherit from?


# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)


# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)

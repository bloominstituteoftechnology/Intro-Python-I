# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

waypoints = [{
    "lat": "34",
    "lon" : "-120",
    "name": "The first waypoint"
}]

waypoints.append({"lat": 55, "lon": 23, "name": "Heaven"})

# YOUR CODE HERE


class LatLon(): 
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
#Pass throught the name of the class you want to inherit from
# Use super to gain access

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __repr__(self):
        return f"Waypoint: {self.name},{self.lat}, {self.lon}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name,lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __repr__(self):
        return f"Geocache : {self.name} , {self.difficulty},{self.size}, {self.lat} {self.lon}"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
#Create a new object for waypoint

waypoints = Waypoint("Catacombs", 42.5433, 55.477)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoints)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache("Newberry Views", 1.5, 2,  44.952137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

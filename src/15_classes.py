# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    lat = int
    lon = int
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):

    '''
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    '''

    def __init__(self, lat, lon, name):
        self.lat = lat
        self.lon = lon
        self.name = name

    def __str__(self):

        return f'name: {self.name}, lat: {self.lat}, lon: {self.lon}'

    name = str
    lat = LatLon.lat
    lon = LatLon.lon


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    '''
        def __init__(self, lat, lon, name):
            super().__init__(lat, lon, name)
            self.name = name

        '''

    def __init__(self, lat, lon, name, size, difficulty):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.size = size
        self.difficulty = difficulty

    def __str__(self):

        return f'name: {self.name}, lat: {self.lat}, lon: {self.lon}, size: {self.size}, difficulty: {self.difficulty}'

    difficulty = int
    size = int
    name = Waypoint.name
    lat = Waypoint.lat
    lon = Waypoint.lon

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
newWP = Waypoint(lat=41.70505, lon=-121.51521, name="Catacombs")
print(newWP)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(newWP)

# Make a new geocache "Newberry Views", diff 1.5, size 2 , 44.052137, -121.41556

# YOUR CODE HERE
newGeo = Geocache(lat=44.052137, lon=-121.41556, name="Newberry Views", difficulty=1.5, size=2)

# Print it--also make this print more nicely
print(newGeo)

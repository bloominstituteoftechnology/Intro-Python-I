# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        print(f'V1 of Print: lat = {lat} // lon = {lon}')

    def __str__(self):
        output = f'__str__ Print: This is the lat: {self.lat}. This is the lon: {self.lon}'
        return output

# Test
testResult = LatLon(5,19)
print(testResult)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        output = f'__str__ Waypoint Print: {self.name} is located at lat: {self.lat}, lon: {self.lon}'
        return output

# Test
waypointTestResult = Waypoint('Starbucks', 1,2)
print(waypointTestResult)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        output = f'__str__ Geocache Print: {self.name} is a {self.size} Geocache and is located at lat: {self.lat}, lon:{self.lon}'
        return output

# Test
geocacheTestResult = Geocache('MyHouse', 'hard','small', 100, 200)
print(geocacheTestResult)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint('NewWaypoint', 50,55)
print(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
newGeocache = Geocache('Newberry Views', 'diff 1.5','size 2', 44.052137, -121.41556)

# Print it--also make this print more nicely
print(newGeocache)

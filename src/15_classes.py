# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)  # Access methods in parent class LatLon
        self.name = name

    # Defines how we want the class to be printed.
    def __str__(self):
        # Returns a string.
        return f"<Waypoint '{self.name}' - {self.lat}, {self.lon}>"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        # Returns a string.
        # Ignoring PEP8 here due to formatting.
        return f"<Geocache '{self.name}', Difficulty: {self.difficulty}, Size: {self.size} - {self.lat}, {self.lon}>"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(name='Catacombs', lat=41.70505, lon=-121.51521)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)  # Complete!

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(name="Newberry Views", difficulty=1.5, size=2,
                    lat=44.052137, lon=-121.41556)
# Print it--also make this print more nicely
print(geocache)  # Complete!

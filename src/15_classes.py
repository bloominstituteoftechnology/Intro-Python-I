# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    """geolocation information as lat & lon"""
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon`
# to the constructor. It should inherit from LatLon. Look up the `super` method


class Waypoint(LatLon):
    """Named location that inherets from LatLon class"""
    def __init__(self, name, *args):
        super().__init__(*args)
        self.name = name

    def __str__(self):
        return f'{self.name} - Lat: {self.lat} | Lon: {self.lon}'


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    """Geocache details that inherets from Waypoint class"""
    def __init__(self, difficulty, size, *args):
        super().__init__(*args)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f'''{self.name} -   Lat: {self.lat} | Lon: {self.lon}
                   Difficulty: {self.difficulty}
                   Size: {self.size}'''


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(1.5, 2, "Newberry Views", 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

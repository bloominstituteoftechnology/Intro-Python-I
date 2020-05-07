# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat: float = None, lon: float = None):
        """Base class for representing location coordinates
        :param lat [float] : Latitude, defaults to None
        :param lon [float] : Longitude, defaults to None
        """
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"@({self.lat}, {self.lon})"
   

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class WayPoint(LatLon):
    def __init__(self, name: str = None, lat: float = None, lon: float = None):
        """Simple class for representing waypoint data.
        :param LatLon (class) : Parent class
        :param name     [str] : Name of the waypoint, defaults to None
        :param lat    [float] : Latitude, defaults to None
        :param lon    [float] : Longitude, defaults to None
        """
        super().__init__(lat=lat, lon=lon)
        self.name = name

    def __str__(self):
        return f"{self.name} @ ({self.lat}, {self.lon})"


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class GeoCache(WayPoint):
    def __init__(
        self,
        name: str = None,
        difficulty: int = None,
        size: float = None,
        lat: float = None,
        lon: float = None,
    ):
        """Class for representing Geocache data. Inherits from WayPoint.
        :param WayPoint (class) : Parent class.
        :param name       [str] : Name of the geocache, defaults to None
        :param difficulty [int] : Difficulty to find (out of 10), defaults to None
        :param size     [float] : Size of the geocache in centimeters, defaults to None
        :param lat      [float] : Latitude of the geocache, defaults to None
        :param lon      [float] : Longitude of the geocache, defaults to None
        """
        super().__init__(name=name, lat=lat, lon=lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"{self.name}: {self.difficulty}/10, {self.size}cm @ ({self.lat}, {self.lon})"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = WayPoint("Catacombs", 41.70505, -121.51521)
print(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = GeoCache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Print it--also make this print more nicely
print(geocache)

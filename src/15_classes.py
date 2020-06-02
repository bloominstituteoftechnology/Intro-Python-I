# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    lat: float
    lon: float

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

point = LatLon(19.9, 39.8)

print(point.lat)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    name: str

    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return f"Name: {self.name}\nLat: {self.lat}\nLon: {self.lon}"

place = Waypoint("someplace", 38.9, 104.5)

print(place.name)
print(place.lat)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    difficulty: float
    size: int

    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        description = super().__str__()
        description += f"\nDifficulty: {self.difficulty}\nSize: {self.size}"
        return description


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

print("")
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)

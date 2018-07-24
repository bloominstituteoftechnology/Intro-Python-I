# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:

    def __init__(self, name, lat, lon):
        self.lat = lat
        self.lon = lon
        self.name = name
        # Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
        # constructor. It should inherit from LatLon.


class Geocache:

    def __init__(self, name, difficulty, size, lat, lon):
        self.name = name
        self.difficulty = difficulty
        self.size = size
        self.lat = lat
        self.lon = lon

        # Make a class Geocache that can be passed parameters `name`, `difficulty`,
        # `size`, `lat`, and `lon` to the constructor. What should it inherit from?


newWaypoint = LatLon('Catacombos', 41.70505, -121.51521)
# Make a new waypoint "Catacombs", 41.70505, -121.51521

# Print it
print('newWaypint', newWaypoint)
# Without changing the following line, how can you make it print into something
# more human-readable?
w = {
    'name': newWaypoint.name,
    'lat': newWaypoint.lat,
    'lon': newWaypoint.lon
}
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
newGeoCache = Geocache("NewBerry Views", 1.5, 2, 44.052137, -121.41556)
g = {
    'name': newGeoCache.name,
    'difficulty': newGeoCache.difficulty,
    'size': newGeoCache.size,
    'lat': newGeoCache.lat,
    'log': newGeoCache.lon
}
# Print it--also make this print more nicely
print(g)

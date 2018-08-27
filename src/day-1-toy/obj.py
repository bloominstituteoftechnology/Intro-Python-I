# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# Make a new waypoint "Catacombs", 41.70505, -121.51521


class Latlon():
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


class Waypoint(Latlon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def get_description(self):
        return (self.name + " is located at " + str(self.lat) + " latitude and " + str(self.lon) + " longitude")


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    # Overriding Waypoint method as there are more parameters to describe than just the ones inherited above.

    def get_description(self):
        return (self.name + " is located at " + str(self.lat) + " latitude and " + str(self.lon) + " longitude. It has a difficulty of " + str(self.difficulty) + " and size of " + str(self.size) + ".")


new_waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
w = new_waypoint.get_description()

# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)


new_geocache = Geocache("Newberry Views", "1.5", "2",
                        "44.052137", "-121.41556")
g = new_geocache.get_description()

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# Print it--also make this print more nicely
print(g)

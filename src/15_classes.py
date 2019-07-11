# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon():
    def __init__(self, lat, lon):
        LatLon.obj_type = 'New' # this is a static variable, shared between objects in a class
        self.lat = lat
        self.lon = lon

# Notes:
# __init__ is a contructor, req to build an instance of a class.
# In a db, instance with be a row
# self refers to the instance


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat,lon)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)
        # For multiple inheritance:
        # LatLon().__init__(name, lat, lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache) # Need to take notes from day2 lecture.

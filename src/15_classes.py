# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

#My test class instantiation
# class ListAlphabet:
#     def __init__(self, *x):
#         alph = [x.upper() for x in x ]
#         print(alph)

# x = ListAlphabet('a', 'b', 'c')

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
latlon = LatLon(41.70505, -121.51521)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def __str__(self):
        return '"Name: {name}"\nLatitude: {lat}\nLongitude: {lon}'.format(name=self.name, lat=self.lat, lon=self.lon)
        
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):    
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)
    
    def __str__(self):
        return '"Name: {name}"\n"Difficulty: {diff}\nSize: {size}\nLatitude: {lat}\nLongitude: {lon}'.format(name=self.name, diff=self.difficulty, size=self.size, lat=self.lat, lon=self.lon)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint("Catacombs", latlon.lat, latlon.lon)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint, end="\n\n")
new_waypoint = Waypoint("Newberry Views", 44.052137, -121.41556)
# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
geocache = Geocache(new_waypoint.name, "diff 1.5", "size 2", new_waypoint.lat, new_waypoint.lon )

# Print it--also make this print more nicely
print(geocache, end="\n\n")

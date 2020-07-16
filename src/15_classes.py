# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class latlon(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return(f'This is the lat {self.lat} and this is the lon {self.lon}')

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class waypoint(latlon):
    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)
        def __str__(self):
            return(f'The name is {self.name}, the lat is {self.lat} and the lon is {self.lon}')
        


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class geocache(waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super(geocache, self).__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def __str__(self): #* I will have to assign the fstring to a variable to split it up but I don't feel like it currently :')
        return(f'''The difficulty is {self.difficulty} and the size is {self.size} The name is {self.name}, the lat is {self.lat} and the lon is {self.lon}''')

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = waypoint('catacombs', 41.70505, -121.51521)
print(waypoint.name, waypoint.lat, waypoint.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint) #! it's not printing the str in my waypoint class???

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = geocache(44.052137, -121.41556, 'Newberry Views', 1.5, 2)

# Print it--also make this print more nicely
print(geocache)

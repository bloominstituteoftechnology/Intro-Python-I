# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    '''
    this thing. technically a class, but doesn't do anything...
    how do I know it actually works!!???!!!
    '''

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    pass

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    '''inherits from LatLon. adds name parameter. still don't do nothin.'''

    def __init__(self, name, lat, lon):
        self.name = name
        super().__init__(lat, lon)

    def __repr__(self):
        return 'name: {} \nlat: {} \nlon: {}'.format(
            self.name, self.lat, self.lon
        )

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    '''inherits from Waypoint. adds difficulty and size parameters'''

    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, lon)

    def __repr__(self):
        return 'name: {} \ndifficulty: {} \nsize: {} \nlat: {} \nlon: {}'.format(
           self.name, self.difficulty, self.size, self.lat, self.lon 
        )

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

kitty = Waypoint('Catacombs', 41.70505, -121.51521)

print(kitty)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

# print(waypoint) ...see above...

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

newbview = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely

print(newbview)

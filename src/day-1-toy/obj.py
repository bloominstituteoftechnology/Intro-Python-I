# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# so it's been a while since I've done anything in Python--wow I'm a little
# more rusty than I thougth lol
class LatLon(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def return_every_damn_thing(self):
        return self.lat, self.lon, self.name

new_waypoint = Waypoint(100, 200, 'leyline')
print(new_waypoint.name)
print(new_waypoint.lat)
print(new_waypoint.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def return_all_the_stuff(self):
        return self.lat, self.lon, self.name, self.difficulty, self.size

new_geo = Geocache(100, 100, 'leyline2', 'superHard', 'kinda big')
print(new_geo.lat, new_geo.lon, new_geo.name, new_geo.difficulty, new_geo.size)
# Make a new waypoint "Catacombs", 41.70505, -121.51521
catacombs = Waypoint(41.70505, -121.51521, 'Catacombs')
# Print it
print(catacombs)
# Without changing the following line, how can you make it print into something
# more human-readable?
w = catacombs.return_every_damn_thing()
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
new_berry_views = Geocache(44.052137, -121.41556, 'Newberry Views', 'really tough', 'pretty darn big')
# Print it--also make this print more nicely
g = new_berry_views.return_all_the_stuff()
print(g)

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return '{{"name": "{}", "latitude": {}, "longitude": {}}}'.format(self.name, self.lat, self.lon)


class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.name = name
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return ('{{"name": "{}", "difficulty": {}, "size": {}, "latitude": {}, "longitude": {}}}'
                .format(self.name, self.difficulty, self.size, self.lat, self.lon))


# Print it
#
# Without changing the following line, how can you make it print into something
# more human-readable?
w = Waypoint('Catacombs', 41.70505, -121.51521)
print(w)

# Print it--also make this print more nicely
g = Geocache('Newberry Views', 1.5, 2, 44.052137, -121.41556)
print(g)

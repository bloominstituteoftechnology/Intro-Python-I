# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def print_coords(self):
        print(f'🗺️  [{self.lat}, {self.lon}]')


hometown = LatLon(40.344688, -111.723091)
print(hometown.lat)
print(hometown.lon)
hometown.print_coords()
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        # LatLon.__init__(self, lat, lon) # One way to do it; using super below is preferred
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return '🗺️  {self.name} -- Latitude: {self.lat} Longitude: {self.lon}'.format(self=self)

    def print_formatted_waypoint(self):
        print(f'🗺️  {self.name} is found at {self.lat}, {self.lon}.')

    def print_for_assignment(self):
        print(f'"{self.name}", {self.lat}, {self.lon}')


disneyland = Waypoint(33.812092, -117.918976, 'Disneyland')
disneyland.print_formatted_waypoint()
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        score = '⭐' * int(self.difficulty)
        if (self.difficulty - int(self.difficulty) != 0):
            score += '➕'

        size_string = str(self.size)
        if (self.size == 1):
            size_string = 'small'
        elif (self.size == 2):
            size_string = 'medium'
        elif (self.size == 3):
            size_string = 'large'
        elif (self.size == 4):
            size_string = 'x-large'

        return f'{self.name} {score} Size: {size_string} Location: [{self.lat},{self.lon}]'

    def print_geocache_details(self):
        print(f'{self.name}: Difficulty: {self.difficulty}, Size: {self.size}, Location: {self.lat}, {self.lon}')


arches_np = Geocache(38.637291, -109.600533,
                     'Arches National Park', 3, 1)
arches_np.print_geocache_details()

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
catacombs = Waypoint(41.70505, -121.51521, "Catacombs")
catacombs.print_for_assignment()


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)
print(catacombs)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE
newberry_views = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)
newberry_views.print_geocache_details()


# Print it--also make this print more nicely
# print(geocache)
print(newberry_views)
print(arches_np)

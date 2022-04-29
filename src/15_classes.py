# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def display(self):
        print("Lat: " + str(self.lat))
        print("Lon: " + str(self.lon))

obj = LatLon(3, 7)
obj.display()

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

# 1st way:
# class Waypoint(LatLon):
#     def __init__(self, name, lat, lon):
#         self.name = name
#         LatLon.lat = lat
#         LatLon.lon = lon
#     def display1(self):
#         print("Name: " + str(self.name), ", Lat: " + str(LatLon.lat), ", Lon: " + str(LatLon.lon))

# obj1 = Waypoint("lauren", 10, 20)
# obj1.display1()

# 2nd way:
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        self.name = name
        super(Waypoint, self).__init__(lat, lon)
    def display_child(self):
        print("Name: " + self.name, ", Lat: " + str(self.lat), ", Lon: " + str(self.lon))
    def __str__(self):
        return 'Waypoint(name='+self.name+', lat='+str(self.lat)+', lon='+str(self.lon)+')'

w = Waypoint("lauren", 10, 20)
w.display_child()

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        self.difficulty = difficulty
        self.size = size
        super(Geocache, self).__init__(name, lat, lon)
    def display_gchild(self):
        print("Name: " + str(self.name), ", Difficulty: " + str(self.difficulty), ", Size: " + str(self.size), ", Lat: " + str(self.lat), ", Lon: " + str(self.lon))
    def __str__(self):
        return 'Geocache(Name: ' + self.name + ', Difficulty: ' + str(self.difficulty) + ', Size: ' + str(self.size) + ', Lat: ' + str(self.lat) + ', Lon: ' + str(self.lon) + ')'

g = Geocache("alex", 5, 33, 15, 20)
g.display_gchild()

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
w2 = Waypoint("Catacombs", 41.70505, -121.51521)
w2.display_child()

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(w2.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
g2 = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(g2.__str__())

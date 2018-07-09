# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoint1 = dict([('latitude', '25* 15\' 10.08" N' ), ('longitude', '55* 21\' 51.84" E'), ('name', 'OMDB')])
waypoint2 = dict([('latitude', '33* 56\' 33.13" N'), ('longitude', '118* 24\' 29.07" W'), ('name', 'KLAX')])
waypoint3 = dict([('latitude', '41* 58\' 42.97" N' ), ('longitude', '87* 54\' 17.43" W'), ('name', 'KORD')])


waypoints = [waypoint1, waypoint2, waypoint3]

for waypoint in waypoints:
    print(waypoint)

# Write a loop that prints out all the field values for all the waypoints

# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Write a loop that prints out all the field values for all the waypoints

def print_waypoints(tuple):
    for waypoint in tuple:
        print("LAT : %s" %waypoint["lat"])
        print("LON : %s" %waypoint["lon"])
        print("NAM : %s" %waypoint["name"])
        print("")

print_waypoints(waypoints)
print("**************")
# Add a new waypoint to the list
waypoints.append({
        "lat": 59,
        "lon": -33,
        "name": "a home"
        })

print_waypoints(waypoints)


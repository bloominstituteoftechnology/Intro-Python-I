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
def print_way():
    for waypoint in waypoints:
        print("%s is at (%d, %d)" %(waypoint["name"], waypoint["lat"], waypoint["lon"]))
print_way()
# Add a new waypoint to the list
new = {"lat": 22, "lon": 32, "name": "no place"}
waypoints.append(new)
print_way()

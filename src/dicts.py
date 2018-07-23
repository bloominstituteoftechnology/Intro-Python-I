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
        "name": "a place",
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

new_waypoint = {
        "lat": 36,
        "lon": -112,
        "name": "North Dakota",
    }
    
# Add a new waypoint to the list
waypoints.append(new_waypoint)
# Write a loop that prints out all the field values for all the waypoints  
# for i in waypoints: //naive way of doing it.. any properties
#     print('------------------------')
#     for j in i:
#         print(j, ':', i[j])
for waypoint in waypoints:
    print("____________________________________________________")
    for prop in waypoint:
        print("{0}:{1}".format(prop, waypoint[prop]))



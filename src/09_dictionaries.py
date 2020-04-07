
# Add a new waypoint to the list
# YOUR CODE HERE

waypoints.append({
    "lat": 46,
    "lon": -128,
    "name": "a fourth place"
})

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE

waypoints[0]["lon"] = -130
waypoints[0]["name"] = "not a real place"

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for waypoint in waypoints:
    print(waypoint.values())

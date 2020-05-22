def jumpingOnClouds(c):
    # c is an array of binary integers ie [0,1,0,0,0,1,0]
    # return shortest path between first 0 to last 0
    '''
    graph = { 0: {2},
                1: set(),
                2: {3, 4},
                3: {4},
                4: {6},
                5: set(),
                6: set()
    '''
    graph = {}
    for i in range(len(c)):
        graph[i] = set()

    for i in range(len(c)):
        # Check if value at i is a 0
        if c[i] == 0:
            # If so, check the value at i+1. If value is 0, then add edge.
            if i < len(c) - 1:
                if c[i+1] == 0:
                    graph[i].add(i+1)
            # Then check value at i+2. Ditto
            if i < len(c) - 2:
                if c[i+2] == 0:
                    graph[i].add(i+2)
    # print(graph)

    def bfs(graph, target):
        queue = []
        visited = set()
        current_node = 0
        queue.append([current_node])

        if current_node == target:
            return queue
        while queue:
            current_path = queue.pop(0)
            current_node = current_path[-1]
            if current_node not in visited:
                neighbors = graph[current_node]
                for neighbor in neighbors:
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == target:
                        print(new_path)
                        return new_path
            visited.add(current_node)
        # print("didn't find it")

    shortest_path = bfs(graph, len(c)-1)  # len(c)-1
    # print(shortest_path)
    # print(len(shortest_path) - 1)
    return len(shortest_path) - 1


jumpingOnClouds([0, 1, 0, 0, 0, 1, 0])

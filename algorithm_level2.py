import heapq
import readFile as r

# manhattan distance
def heuristics(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def GBFS_level2(matrix, start, goal, time):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    explored_node = []
    heapq.heappush(explored_node, (0, start, 0))
    came_from = {}
    came_from[start] = None
    
    while explored_node:
        _, current, current_time = heapq.heappop(explored_node)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, current_time
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != '-1':
                additional_time = 1
                if matrix[neighbor[0]][neighbor[1]].isdigit():
                    additional_time += int(matrix[neighbor[0]][neighbor[1]])
                new_time = additional_time + current_time
                if neighbor not in came_from and new_time <= time:
                    priority = heuristics(neighbor, goal)
                    heapq.heappush(explored_node, (priority, neighbor, new_time))
                    came_from[neighbor] = current

    return [], -1

def A_star_level2(matrix, start, goal, time):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    explored_node = []
    heapq.heappush(explored_node, (0, start, 0))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while explored_node:
        _, current, current_time = heapq.heappop(explored_node)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, current_time
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != '-1':
                additional_time = 1
                new_cost = cost_so_far[current] + 1
                if isinstance(matrix[neighbor[0]][neighbor[1]], int):
                    additional_time += matrix[neighbor[0]][neighbor[1]]
                new_time = additional_time + current_time
                if (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]) and (new_time <= time):
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristics(neighbor, goal)
                    heapq.heappush(explored_node, (priority, neighbor, new_time))
                    came_from[neighbor] = current

    return [], -1 

def print_path_level2(path, time_spent):
    if not path:
        print("No path found")
    else:
        print("Path:")
        for node in path:
            print(node, end=" -> ")
        print("Goal")
        print(f"Time spent: {time_spent} minutes")


# testing level 2
# filename = 'input1_level1.txt'
# n, m, t, f, matrix = r.read_input(filename)
# positions = r.find_positions(matrix, n, m)
# start = positions['S1']
# goal = positions['G1']

# if start and goal:
#     path, time_spent = A_star_level2(matrix, start, goal, t)
#     print_path_level2(path, time_spent)
# else:
#     print("Start or goal position not found in the matrix.")
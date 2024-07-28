from collections import deque

def bfs_level3(matrix, start, goal, max_time, toll_booths, max_fuel, fuel_stations):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(start, 0, max_fuel)])  # (position, time, fuel)
    came_from = {}
    cost_so_far = {}
    
    start_state = (start, max_fuel)
    came_from[start_state] = None
    cost_so_far[start_state] = 0
    
    while queue:
        current, current_time, current_fuel = queue.popleft()
        
        if current == goal:
            path = []
            state = (current, current_fuel)
            while state:
                path.append(state[0])
                state = came_from[state]
            path.reverse()
            return path
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != -1:
                new_time = current_time + 1
                new_fuel = current_fuel - 1
                if neighbor in toll_booths:
                    new_time += toll_booths[neighbor]
                if neighbor in fuel_stations:
                    new_fuel = max_fuel
                
                new_state = (neighbor, new_fuel)
                
                if new_fuel >= 0 and new_time <= max_time:
                    # If neighbor has not been visited or we found a better path to it
                    if (new_state not in cost_so_far) or (new_time < cost_so_far[new_state]):
                        queue.append((neighbor, new_time, new_fuel))
                        cost_so_far[new_state] = new_time
                        came_from[new_state] = (current, current_fuel)

    return []

# Test main function for Level 3
# def main_level3():
#     matrix = [
#         [0, 0, 0, 0, -1, -1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, -1, 0, -1],
#         [0, 0, -1, -1, -1, 0, 0, -1, 0, -1],
#         [0, 0, 0, 0, -1, 0, 0, -1, 0, 0],
#         [0, 0, -1, -1, -1, 0, 0, -1, -1, 0],
#         [0, 0, -1, 0, 0, 0, 0, 0, -1, 0],
#         [0, 0, 0, 0, -1, 0, -1, 0, -1, 0],
#         [0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
#         [0, -1, -1, -1, -1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, -1, -1, -1, 0]
#     ]
#     start = (1, 1)
#     goal = (7, 8)
#     max_time = 20
#     toll_booths = {(5, 0): 1, (6, 5): 4, (6, 7): 8, (9, 2): 5}
#     max_fuel = 10
#     fuel_stations = {(6, 2): 1}
    
#     path = bfs_level3(matrix, start, goal, max_time, toll_booths, max_fuel, fuel_stations)
#     if path:
#         print("Level 3 Path:", path)
#     else:
#         print("No path found within the given constraints.")

# main_level3()

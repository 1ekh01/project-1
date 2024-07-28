from collections import deque
import heapq

# Heuristic func
def heuristics(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# BFS
def BFS(matrix, start, goal):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([start])
    came_from = {}
    came_from[start] = None
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != '-1':
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

    return []

# DFS
def DFS(city_map, start, goal):
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stack = [start]
    visited = set()
    parent = {}
    
    while stack:
        current = stack.pop()
        if current == goal:
            break
        
        for move in movements:
            next_cell = (current[0] + move[0], current[1] + move[1])
            
            if (0 <= next_cell[0] < len(city_map) and 
                0 <= next_cell[1] < len(city_map[0]) and 
                city_map[next_cell[0]][next_cell[1]] != -1 and
                next_cell not in visited):
                
                stack.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

    path = []
    if goal in parent:
        path.append(goal)
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
    
    return path

# UCS
def UCS(matrix, start, goal):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    explored_node = []
    heapq.heappush(explored_node, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while explored_node:
        current_cost, current = heapq.heappop(explored_node)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != '-1':
                new_cost = current_cost + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost
                    heapq.heappush(explored_node, (priority, neighbor))
                    came_from[neighbor] = current

    return []

# GBFS
def GBFS(matrix, start, goal):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    explored_node = []
    heapq.heappush(explored_node, (0, start))
    came_from = {}
    came_from[start] = None
    
    while explored_node:
        _, current = heapq.heappop(explored_node)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != '-1':
                if neighbor not in came_from:
                    priority = heuristics(neighbor, goal)
                    heapq.heappush(explored_node, (priority, neighbor))
                    came_from[neighbor] = current

    return []

# A*
def A_star(matrix, start, goal):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    explored_node = []
    heapq.heappush(explored_node, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while explored_node:
        _, current = heapq.heappop(explored_node)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != '-1':
                new_cost = cost_so_far[current] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristics(neighbor, goal)
                    heapq.heappush(explored_node, (priority, neighbor))
                    came_from[neighbor] = current

    return []

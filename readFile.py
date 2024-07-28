def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    first_line = lines[0].strip().split()
    n = int(first_line[0])
    m = int(first_line[1])
    t = int(first_line[2])
    f = int(first_line[3])

    matrix = []
    for i in range(1, n + 1):
        row = lines[i].strip().split()
        matrix.append(row)
    
    return n, m, t, f, matrix

def find_positions(matrix, n, m):
    positions = {'S': None, 'G': None, 'S1': None, 'G1': None, 'S2': None, 'G2': None}

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                positions['S'] = (i, j)
            elif matrix[i][j] == 'G':
                positions['G'] = (i, j)
            elif matrix[i][j] == 'S1':
                positions['S1'] = (i, j)
            elif matrix[i][j] == 'G1':
                positions['G1'] = (i, j)
            elif matrix[i][j] == 'S2':
                positions['S2'] = (i, j)
            elif matrix[i][j] == 'G2':
                positions['G2'] = (i, j)
    
    return positions

def print_path(algorithm_name, start_label, path):
    if not path:
        print(f"No path found from {start_label} using {algorithm_name}")
    else:
        print(f"{start_label}")
        print(f"{algorithm_name} path: ", end="")
        for node in path:
            print(node, end=" -> ")
        print("Goal")




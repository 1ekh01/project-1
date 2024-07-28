def read_input_level3(filename):
    with open(filename, 'r') as file:
        n, m, t, f = map(int, file.readline().strip().split())
        matrix = []
        toll_booths = {}
        fuel_stations = {}
        
        for i in range(n):
            row = file.readline().strip().split()
            for j in range(m):
                if row[j].startswith('T'):
                    toll_booths[(i, j)] = int(row[j][1:])
                    row[j] = '0'
                elif row[j].startswith('F'):
                    fuel_stations[(i, j)] = 1  # Assuming all fuel stations refill to max fuel
                    row[j] = '0'
                elif row[j] == 'S':
                    start = (i, j)
                    row[j] = '0'
                elif row[j] == 'G':
                    goal = (i, j)
                    row[j] = '0'
                row[j] = int(row[j]) if row[j] != '-1' else -1
            matrix.append(row)
        
    return n, m, t, f, matrix, start, goal, toll_booths, fuel_stations

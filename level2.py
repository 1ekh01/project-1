import os
from readFile import read_input, find_positions
from algorithm_level2 import A_star_level2 as alg2

def format_path(path):
    return " -> ".join(f"({x},{y})" for x, y in path)

def process_file_level2(filename, output_filename):
    n, m, t, f, matrix = read_input(filename)
    positions = find_positions(matrix, n, m)
    start = positions['S']
    goal = positions['G']
    
    if start and goal:
        path, time_spent = alg2(matrix, start, goal, t)
        os.makedirs('results', exist_ok=True)
        output_filepath = os.path.join('results', output_filename)
        with open(output_filepath, 'w') as f:
            if path:
                f.write(f"Path:\n{format_path(path)}\n")
                f.write(f"Time spent: {time_spent} minutes\n")
            else:
                f.write("No path found\n")
    else:
        print("Start or goal position not found in the matrix.")

    print(f"Results written to {output_filepath}")

def level2(directory):
    files = [f for f in os.listdir(directory) if f.startswith('input') and '_level2.txt' in f]
    files.sort()
    
    print("Available files:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}: {file}")
    
    file_number = int(input("Choose a file to process: "))
    if 1 <= file_number <= len(files):
        selected_file = files[file_number - 1]
        filepath = os.path.join(directory, selected_file)
        output_filename = f"output{file_number}_level2.txt"
        process_file_level2(filepath, output_filename)
    else:
        print("Invalid number. Please try again.")

if __name__ == "__main__":
    level2('samples')

import os
import readFile as r1
import algorithm_level1 as alg1

def format_path(path):
    return " -> ".join(f"({x},{y})" for x, y in path)

def process_file(filename, output_filename):
    n, m, t, f, matrix = r1.read_input(filename)
    print(f"Processing {filename}")
    
    positions = r1.find_positions(matrix, n, m)
    start = positions['S']
    goal = positions['G']
    
    paths = {
        "BFS": alg1.BFS(matrix, start, goal),
        "DFS": alg1.DFS(matrix, start, goal),
        "UCS": alg1.UCS(matrix, start, goal),
        "GBFS": alg1.GBFS(matrix, start, goal),
        "A*": alg1.A_star(matrix, start, goal)
    }
    
    os.makedirs('results', exist_ok=True)
    output_filepath = os.path.join('results', output_filename)
    with open(output_filepath, 'w') as f:
        for name, path in paths.items():
            f.write(f"{name} path:\n")
            if path:
                f.write(f"S\n{format_path(path)}\n")
            else:
                f.write("No path found\n")
            f.write("\n")

    print(f"Results written to {output_filepath}")

def level1(directory):
    files = [f for f in os.listdir(directory) if f.startswith('input') and '_level1.txt' in f]
    files.sort()

    print("Available files:")
    for idx, filename in enumerate(files):
        print(f"{idx + 1}: {filename}")

    file_number = int(input("Choose a file to process: "))
    if 1 <= file_number <= len(files):
        selected_file = files[file_number - 1]
        filepath = os.path.join(directory, selected_file)
        output_filename = f"output{file_number}_level1.txt"
        process_file(filepath, output_filename)
    else:
        print("Invalid number. Please try again.")

if __name__ == "__main__":
    level1('samples')

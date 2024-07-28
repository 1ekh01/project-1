import os
import readFile_level3 as r3
import algorithm_level3 as alg3

def format_path(path):
    return "[" + ", ".join(f"({x},{y})" for x, y in path) + "]"

def process_file_level3(filename, output_filename):
    n, m, t, f, matrix, start, goal, toll_booths, fuel_stations = r3.read_input_level3(filename)
    print(f"Processing {filename}")

    if start and goal:
        path = alg3.bfs_level3(matrix, start, goal, t, toll_booths, f, fuel_stations)
        os.makedirs('results', exist_ok=True)
        output_filepath = os.path.join('results', output_filename)
        with open(output_filepath, 'w') as f:
            if path:
                f.write(f"Level 3 Path:\n{format_path(path)}\n")
            else:
                f.write("No path found within the given constraints.\n")
    else:
        print("Start or goal position not found in the matrix.")

    print(f"Results written to {output_filepath}")

def level3(directory):
    files = [f for f in os.listdir(directory) if f.startswith('input') and '_level3.txt' in f]
    files.sort()

    print("Available files:")
    for idx, filename in enumerate(files):
        print(f"{idx + 1}: {filename}")

    file_number = int(input("Choose a file to process: "))
    if 1 <= file_number <= len(files):
        selected_file = files[file_number - 1]
        filepath = os.path.join(directory, selected_file)
        output_filename = f"output{file_number}_level3.txt"
        process_file_level3(filepath, output_filename)
    else:
        print("Invalid number. Please try again.")

if __name__ == "__main__":
    level3('samples')

import os
import readFile_level3 as r3
import algorithm_level3 as alg3

def process_file_level3(filename):
    n, m, t, f, matrix, start, goal, toll_booths, fuel_stations = r3.read_input_level3(filename)
    print(f"Processing {filename}")
    print(n, m, t, f)
    
    for row in matrix:
        print(" ".join(map(str, row)))
    
    if start and goal:
        path = alg3.bfs_level3(matrix, start, goal, t, toll_booths, f, fuel_stations)
        if path:
            print("Level 3 Path:", path)
        else:
            print("No path found within the given constraints.")
    else:
        print("Start or goal position not found in the matrix.")
    print("\n")

def level3(directory):
    files = [f for f in os.listdir(directory) if f.startswith('input') and '_level3.txt' in f]
    files.sort()

    print("Available files:")
    for idx, filename in enumerate(files):
        print(f"{idx + 1}: {filename}")

    file_number = int(input("Enter the number of the file you want to process: "))
    if 1 <= file_number <= len(files):
        selected_file = files[file_number - 1]
        filepath = os.path.join(directory, selected_file)
        process_file_level3(filepath)
    else:
        print("Invalid number. Please try again.")

if __name__ == "__main__":
    level3('samples')

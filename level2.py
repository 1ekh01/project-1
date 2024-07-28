# level2.py
import os
from readFile import read_input, find_positions
from algorithm_level2 import A_star_level2, print_path_level2

def process_file_level2(filename):
    n, m, t, f, matrix = read_input(filename)
    positions = find_positions(matrix, n, m)
    start = positions['S']
    goal = positions['G']
    
    if start and goal:
        path, time_spent = A_star_level2(matrix, start, goal, t)
        print_path_level2(path, time_spent)
    else:
        print("Start or goal position not found in the matrix.")

def level2(directory):
    files = [f for f in os.listdir(directory) if f.startswith('input') and '_level2.txt' in f]
    files.sort()  # Ensure files are sorted if necessary
    
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    choice = int(input("Choose a file to process: ")) - 1
    if 0 <= choice < len(files):
        process_file_level2(os.path.join(directory, files[choice]))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    level2('samples')

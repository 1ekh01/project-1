import os
import readFile as r
import algorithm_level1 as alg1

def process_file(filename):
    n, m, t, f, matrix = r.read_input(filename)
    print(f"Processing {filename}")
    print(n, m, t, f)

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], " ", end="")
        print("")

    positions = r.find_positions(matrix, n, m)
    start = positions['S']
    goal = positions['G']

    path_BFS = alg1.BFS(matrix, start, goal)
    path_DFS = alg1.DFS(matrix, start, goal)
    path_UCS = alg1.UCS(matrix, start, goal)
    path_GBFS = alg1.GBFS(matrix, start, goal)
    path_A_star = alg1.A_star(matrix, start, goal)

    r.print_path("BFS", "S", path_BFS)
    r.print_path("DFS", "S", path_DFS)
    r.print_path("UCS", "S", path_UCS)
    r.print_path("GBFS", "S", path_GBFS)
    r.print_path("A*", "S", path_A_star)
    print("\n")

def level1(directory):
    files = [f for f in os.listdir(directory) if f.startswith('input') and '_level1.txt' in f]
    files.sort()  # Ensure files are sorted if necessary

    print("Available files:")
    for idx, filename in enumerate(files):
        print(f"{idx + 1}: {filename}")

    file_number = int(input("Enter the number of the file you want to process: "))
    if 1 <= file_number <= len(files):
        selected_file = files[file_number - 1]
        filepath = os.path.join(directory, selected_file)
        process_file(filepath)
    else:
        print("Invalid number. Please try again.")

if __name__ == "__main__":
    level1('samples')

import os
import sys

# Add the current directory to sys.path to resolve module imports correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from level1 import level1
from level2 import level2
from level3 import level3

def main():
    while True:
        print("Choose a level to run:")
        print("1. Level 1")
        print("2. Level 2")
        print("3. Level 3")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            level1('samples')
        elif choice == '2':
            level2('samples')
        elif choice == '3':
            level3('samples')
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 0.")

if __name__ == "__main__":
    main()

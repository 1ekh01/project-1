# Project

CSC14003 - Introduction to Artificial Intelligence.

Project to find the path from the delivery vehicle to the customer.

Members' information:

1. Nguyễn Thế Trung - 22127429
2. Cao Phạm Hoàng Thái - 22127382'
3. Bùi Lê Khôi - 22127205
4. Nguyễn Gia Phúc - 22127331

## Source code Folder Structure

    project
    ├── samples/
    │ ├── input1_level1.txt
    │ ├── input1_level2.txt
    │ ├── input1_level3.txt
    │ ├── ...
    ├── main.py
    ├── algorithm_level1.py
    ├── algorithm_level2.py
    ├── algorithm_level3.py
    ├── level1.py
    ├── level2.py
    ├── level3.py
    ├── readFile.py
    ├── readFile_level3.py

### Description

- **samples/**: Contains test cases, which are input files for different levels.

  - `input1_level1.txt`: Sample input file 1 for level 1.
  - `input1_level2.txt`: Sample input file 1 for level 2.
  - `input1_level3.txt`: Sample input file 1 for level 3.
  - `input2_level1.txt`: Sample input file 2 for level 1.
  - `...`: Other sample input files.

- **main.py**: The main entry point of the project. Users can choose the level and the corresponding input file to process.

- **algorithm_level*n*.py**: Contains algorithms specific to level n.

- **level*n*.py**: Handles operations and logic for level n.

- **readFile.py**: Contains functions to read input files for levels 1 and 2.

- **readFile_level3.py**: Contains functions to read input files specifically for level 3.

## How to Run

To run the project, follow these steps:

1. Ensure you have Python installed on your system. Python 3.x is recommended.

2. Navigate to the project directory.

3. Run the `main.py` script using Python:

```bash
python main.py
```

4. The program will prompt you to choose a level by typing a number:

   - Type 1 for level 1.

   - Type 2 for level 2.

   - Type 3 for level 3.

   - Type 0 to exit. Any other input will notify you of an invalid choice.

5. Follow the instructions on the terminal to proceed with the chosen level.

For example:

```bash
python main.py
Choose a level (1, 2, 3) or 0 to exit: 1
Processing Level 1...
Choose an input file (1, 2, 3, ...) or 0 to go back: 1
```

This will process input1_level1.txt using the algorithms and logic defined in level1.py and algorithm_level1.py.

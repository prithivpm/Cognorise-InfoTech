size = 9

def print_grid(grid):
    for i in range(size):
        for j in range(size):
            print(grid[i][j], end=" ")
        print()

def is_safe(grid, row, col, num):
    for i in range(size):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(grid, row, col):
    if row == size - 1 and col == size:
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)
    for num in range(1, size + 1):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False

def get_sudoku_from_user():
    print("Enter the Sudoku puzzle (row-wise), use 0 to represent empty cells:")
    grid = []
    for _ in range(size):
        row = list(map(int, input().split()))
        grid.append(row)
    return grid

grid = get_sudoku_from_user()

print("\nSolving Sudoku...")
if solve_sudoku(grid, 0, 0):
    print("\nSudoku Solved:")
    print_grid(grid)
else:
    print("No solution exists for the Sudoku puzzle.")

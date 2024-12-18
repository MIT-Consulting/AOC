def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_xmas(grid):
    return count_xmas_occurrences(grid) > 0

def count_xmas_occurrences(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    target = "XMAS"
    
    # Helper function to check if a word exists starting from a position in a given direction
    def check_direction(row, col, dx, dy):
        if (row + 3*dx < 0 or row + 3*dx >= rows or 
            col + 3*dy < 0 or col + 3*dy >= cols):
            return False
        
        for i in range(4):
            if grid[row + i*dx][col + i*dy] != target[i]:
                return False
        return True
    
    # All possible directions: right, left, down, up, and all diagonals
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]
    
    # Check each position as a potential starting point
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1
                    
    return count

def check_mas(grid, start_row, start_col, dx, dy):
    """Check if MAS exists in direction (dx, dy) starting from (start_row, start_col)"""
    rows, cols = len(grid), len(grid[0])
    
    # Get the three characters in the direction
    chars = []
    for i in range(3):
        r = start_row + i*dx
        c = start_col + i*dy
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        chars.append(grid[r][c])
    
    # Check both forward (MAS) and reverse (SAM)
    word = ''.join(chars)
    return word == "MAS" or word == "SAM"

def count_x_mas_patterns(grid):
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # For each potential center point
    for i in range(1, rows-1):  # Need room for the full X pattern
        for j in range(1, cols-1):
            # Check if center is 'A'
            if grid[i][j] != 'A':
                continue
            
            # Check both possible X patterns:
            # Pattern 1: Starting from top corners, going down
            if (check_mas(grid, i-1, j-1, 1, 1) and 
                check_mas(grid, i-1, j+1, 1, -1)):
                count += 1
                continue
            
            # Pattern 2: Starting from bottom corners, going up
            if (check_mas(grid, i+1, j-1, -1, 1) and 
                check_mas(grid, i+1, j+1, -1, -1)):
                count += 1
    
    return count

def solve_part1(filename):
    grid = read_input(filename)
    return count_xmas_occurrences(grid)

def solve_part2(filename):
    grid = read_input(filename)
    return count_x_mas_patterns(grid)

if __name__ == "__main__":
    result1 = solve_part1("Day 4/input.txt")
    print(f"Part 1 Answer: {result1}")
    result2 = solve_part2("Day 4/input.txt")
    print(f"Part 2 Answer: {result2}") 
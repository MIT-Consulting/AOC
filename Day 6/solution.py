from typing import List, Set, Tuple, Optional
from enum import Enum
from collections import deque

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def turn_right(self):
        directions = list(Direction)
        current_index = directions.index(self)
        return directions[(current_index + 1) % 4]

def parse_grid(input_text: str) -> Tuple[Set[Tuple[int, int]], Tuple[int, int], Direction, int, int]:
    lines = input_text.strip().split('\n')
    height = len(lines)
    width = len(lines[0])
    obstacles = set()
    start_pos = None
    start_dir = None
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.add((x, y))
            elif char == '^':
                start_pos = (x, y)
                start_dir = Direction.UP
    
    return obstacles, start_pos, start_dir, width, height

def is_in_bounds(pos: Tuple[int, int], width: int, height: int) -> bool:
    x, y = pos
    return 0 <= y < height and 0 <= x < width

def get_next_pos(pos: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
    return (pos[0] + direction.value[0], pos[1] + direction.value[1])

def simulate_path(obstacles: Set[Tuple[int, int]], start_pos: Tuple[int, int], 
                 start_dir: Direction, width: int, height: int, max_steps: int = 10000) -> bool:
    pos = start_pos
    direction = start_dir
    state_history = [(pos, direction)]
    states_set = {(pos, direction)}
    steps = 0
    
    while steps < max_steps:
        next_pos = get_next_pos(pos, direction)
        
        if not is_in_bounds(next_pos, width, height):
            return False
            
        if next_pos in obstacles:
            direction = direction.turn_right()
            new_state = (pos, direction)
            if new_state in states_set:
                return True
            states_set.add(new_state)
            state_history.append(new_state)
        else:
            pos = next_pos
            new_state = (pos, direction)
            if new_state in states_set:
                return True
            states_set.add(new_state)
            state_history.append(new_state)
        
        steps += 1
    
    return False

def get_original_path(obstacles: Set[Tuple[int, int]], start_pos: Tuple[int, int], 
                     start_dir: Direction, width: int, height: int) -> Set[Tuple[int, int]]:
    pos = start_pos
    direction = start_dir
    path = {pos}
    
    while True:
        next_pos = get_next_pos(pos, direction)
        
        if not is_in_bounds(next_pos, width, height):
            break
            
        if next_pos in obstacles:
            direction = direction.turn_right()
        else:
            pos = next_pos
            path.add(pos)
    
    return path

def solve_part1(input_text: str) -> int:
    obstacles, start_pos, start_dir, width, height = parse_grid(input_text)
    return len(get_original_path(obstacles, start_pos, start_dir, width, height))

def solve_part2(input_text: str) -> int:
    obstacles, start_pos, start_dir, width, height = parse_grid(input_text)
    
    # Get the original path
    original_path = get_original_path(obstacles, start_pos, start_dir, width, height)
    loop_positions = set()
    
    # Get positions adjacent to the original path
    candidates = set()
    for x, y in original_path:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (x + dx, y + dy)
            if (is_in_bounds(new_pos, width, height) and 
                new_pos not in obstacles and 
                new_pos != start_pos and
                new_pos not in original_path):
                candidates.add(new_pos)
    
    # Try each candidate position
    for pos in candidates:
        test_obstacles = obstacles | {pos}
        if simulate_path(test_obstacles, start_pos, start_dir, width, height):
            loop_positions.add(pos)
    
    return len(loop_positions)

# Tests
def test_example():
    example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    
    assert solve_part1(example) == 41
    assert solve_part2(example) == 6

def test_turn_right():
    assert Direction.UP.turn_right() == Direction.RIGHT
    assert Direction.RIGHT.turn_right() == Direction.DOWN
    assert Direction.DOWN.turn_right() == Direction.LEFT
    assert Direction.LEFT.turn_right() == Direction.UP

if __name__ == "__main__":
    # Run tests
    test_example()
    test_turn_right()
    print("All tests passed!")
    
    # Solve actual input
    with open("Day 6/input.txt", "r") as f:
        input_text = f.read()
    
    result = solve_part2(input_text)
    print(f"Solution: {result}") 
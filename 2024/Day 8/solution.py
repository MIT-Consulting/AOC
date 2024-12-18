import math
import itertools
import os

def read_input(filename):
    """Read and parse the input file."""
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return [list(i) for i in data]

def create_mapping(data):
    """Create a coordinate mapping of the grid."""
    mapping = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            mapping[(i, j)] = data[i][j]
    return mapping

def find_antennas(data, mapping):
    """Find all antennas and group them by frequency."""
    antennaInfo = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if mapping[(i, j)] != ".":
                if mapping[(i, j)] not in antennaInfo:
                    antennaInfo[mapping[(i, j)]] = [(i, j)]
                else:
                    antennaInfo[mapping[(i, j)]].append((i, j))
    return antennaInfo

def solve_part1(data, mapping, antennaInfo):
    """Solve part 1: Find antinodes at specific distances."""
    bounds = len(data[0])
    locations = []
    
    for key in antennaInfo:
        for pair in itertools.product(antennaInfo[key], repeat=2):
            if pair[0] != pair[1]:
                dX = pair[1][0] - pair[0][0]
                dY = pair[1][1] - pair[0][1]
                antinode0 = (pair[0][0]-dX, pair[0][1]-dY)
                if antinode0[0] >= 0 and antinode0[0] < bounds and antinode0[1] >= 0 and antinode0[1] < bounds:
                    if antinode0 not in locations:
                        locations.append(antinode0)
                antinode1 = (pair[1][0]+dX, pair[1][1]+dY)
                if antinode1[0] >= 0 and antinode1[0] < bounds and antinode1[1] >= 0 and antinode1[1] < bounds:
                    if antinode1 not in locations:
                        locations.append(antinode1)
    
    return len(locations)

def solve_part2(data, mapping, antennaInfo):
    """Solve part 2: Find antinodes considering resonant harmonics."""
    bounds = len(data[0])
    locations = []
    
    for key in antennaInfo:
        for pair in itertools.product(antennaInfo[key], repeat=2):
            if pair[0] != pair[1]:
                dX = pair[1][0] - pair[0][0]
                dY = pair[1][1] - pair[0][1]
                
                # Add the antenna positions themselves
                if pair[0] not in locations:
                    locations.append(pair[0])
                if pair[1] not in locations:
                    locations.append(pair[1])
                
                # Handle vertical lines
                if dX == 0:
                    for i in range(bounds):
                        point = (i, pair[0][1])
                        if point not in locations:
                            locations.append(point)
                
                # Handle horizontal lines
                elif dY == 0:
                    for i in range(bounds):
                        point = (pair[0][0], i)
                        if point not in locations:
                            locations.append(point)
                
                # Handle diagonal lines
                else:
                    if math.gcd(abs(dX), abs(dY)) != 0:
                        gcd = math.gcd(abs(dX), abs(dY))
                        dX = dX // gcd  # Use integer division
                        dY = dY // gcd
                    
                    # Check antinodes in both directions
                    curr = (pair[0][0], pair[0][1])
                    while 0 <= curr[0] < bounds and 0 <= curr[1] < bounds:
                        if curr not in locations:
                            locations.append(curr)
                        curr = (curr[0] - dX, curr[1] - dY)
                    
                    curr = (pair[1][0], pair[1][1])
                    while 0 <= curr[0] < bounds and 0 <= curr[1] < bounds:
                        if curr not in locations:
                            locations.append(curr)
                        curr = (curr[0] + dX, curr[1] + dY)
    
    return len(locations)

def main():
    """Main function to run the solution."""
    # Read and parse input
    data = read_input('Day 8/input.txt')
    mapping = create_mapping(data)
    antennaInfo = find_antennas(data, mapping)
    
    # Check if area is square
    if len(data[0]) != len(data):
        print("Area Not a Square! Tread with caution!")
    
    # Solve both parts
    part1_answer = solve_part1(data, mapping, antennaInfo)
    part2_answer = solve_part2(data, mapping, antennaInfo)
    
    print(f"Part 1 answer: {part1_answer}")
    print(f"Part 2 answer: {part2_answer}")

if __name__ == "__main__":
    main() 
# Day 8: Resonant Collinearity

## Problem Description

### Part 1
Easter Bunny installation has antennas that need to be analyzed:
- Each antenna has a specific frequency (lowercase letter, uppercase letter, or digit)
- Antinodes occur at points perfectly in line with two antennas of same frequency
- For any pair of same-frequency antennas, antinodes occur at:
  - One point at same distance before first antenna
  - One point at same distance after second antenna
- Need to count unique antinode locations within map bounds

### Part 2
Updated model considering resonant harmonics:
- Antinodes now occur at any grid position exactly in line with two or more same-frequency antennas
- Distance between antennas no longer matters
- Antenna positions themselves count as antinodes if they're in line with another antenna of same frequency
- All points along the line between same-frequency antennas are antinodes
- Need to count total unique antinode locations with new rules

## Approach
- Part 1: Implemented antinode finder:
  - Parse grid to map antenna positions by frequency
  - For each frequency group, find antenna pairs
  - Calculate antinode positions at specific distances
  - Track unique locations within bounds
- Part 2: Extended solution to:
  - Include antenna positions as antinodes
  - Handle vertical, horizontal, and diagonal lines
  - Use GCD for diagonal step calculation
  - Track all points along antenna lines

## Solutions
- Part 1: Number of unique antinode locations = 291
- Part 2: Number of unique antinode locations with resonant harmonics = 1015

## Implementation
Solution implemented in Python (`solution.py`) with:
- Grid parsing and coordinate mapping
- Antenna frequency grouping
- Vector-based antinode calculation
- Line-drawing algorithms for all directions
- Efficient point tracking using lists 
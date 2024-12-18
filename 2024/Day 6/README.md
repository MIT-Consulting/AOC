# Day 6: Guard Gallivant

## Problem Description

### Part 1
Track a guard's patrol path in a lab based on simple movement rules:
- Guard starts at position marked with `^` (facing up)
- Movement rules:
  - If there's an obstacle (`#`) ahead, turn right 90 degrees
  - Otherwise, move forward one step
- Need to count distinct positions visited before guard leaves the map area

### Part 2
Find positions where adding a new obstacle would trap the guard in a loop:
- Can add exactly one new obstacle
- Cannot place obstacle at guard's starting position
- Need to find all possible positions that would create a loop
- Must minimize time paradoxes by having multiple options

## Approach
- Part 1: Implemented path tracking:
  - Parse grid and find start position/direction
  - Follow movement rules until guard leaves map
  - Track all visited positions
  - Count unique positions
- Part 2: Extended solution to:
  - Find all positions adjacent to original path
  - Test each candidate position by adding obstacle
  - Simulate path to check for loops
  - Count valid positions that create loops

## Solutions
- Part 1: Guard visits 4580 distinct positions
- Part 2: Found 1480 possible positions for new obstacle

## Implementation
Solution implemented in Python (`solution.py`) with:
- Enum class for directions
- Grid parsing and bounds checking
- Path simulation and loop detection
- Comprehensive test cases 
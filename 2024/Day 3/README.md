# Day 3: Mull It Over

## Problem Description

### Part 1
The problem involves parsing corrupted computer memory to find valid multiplication instructions. Valid instructions:
- Must be in the format `mul(X,Y)` where X and Y are 1-3 digit numbers
- No spaces allowed anywhere in the instruction
- Must have proper parentheses
- Must ignore any invalid characters or malformed instructions

### Part 2
Introduces control flow instructions:
- `do()`: Enables future multiplication instructions
- `don't()`: Disables future multiplication instructions
- Instructions start enabled by default
- Only the most recent do/don't instruction applies

## Approach
- Part 1: Used regex pattern matching to:
  - Find valid mul(X,Y) instructions
  - Validate format and numbers
  - Handle consecutive instructions
  - Sum up all valid multiplications
- Part 2: Extended solution to:
  - Track enabled/disabled state
  - Process do/don't instructions
  - Only perform multiplications when enabled

## Solutions
- Part 1: Sum of all valid multiplications = 160672468
- Part 2: Sum of enabled multiplications = 84893551

## Implementation
Solution implemented in Python (`solve.py`) using regular expressions for pattern matching and state tracking. 
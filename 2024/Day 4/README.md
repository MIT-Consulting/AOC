# Day 4: Ceres Search

## Problem Description

### Part 1
A word search puzzle where you need to find all occurrences of "XMAS". The word can appear:
- Horizontally
- Vertically
- Diagonally
- Backwards
- Overlapping with other instances

### Part 2
The puzzle is actually an X-MAS puzzle where you need to find patterns of "MAS" forming an X shape:
```
M.S
.A.
M.S
```
- Each MAS in the X can be written forwards or backwards (SAM)
- The center must be 'A'
- Both diagonal MAS/SAM patterns must be present to count as one X-MAS

## Approach
- Part 1: Implemented grid search to:
  - Check all 8 possible directions from each position
  - Handle overlapping and backwards occurrences
  - Count total valid occurrences
- Part 2: Modified search to:
  - Find center 'A' characters
  - Check diagonal patterns for MAS/SAM
  - Validate complete X patterns

## Solutions
- Part 1: Found 2378 occurrences of "XMAS"
- Part 2: Found 1796 X-MAS patterns

## Implementation
Solution implemented in Python (`day4.py`) with unit tests in `test_day4.py`. 
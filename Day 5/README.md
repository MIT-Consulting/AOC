# Day 5: Print Queue

## Problem Description

### Part 1
The problem involves validating the order of pages in safety manual updates based on ordering rules:
- Rules are in the format `X|Y`, meaning page X must be printed before page Y
- Each update is a list of page numbers that need to be printed
- Only rules involving pages in the current update apply
- Need to find updates that are already in correct order
- Calculate sum of middle page numbers from correctly ordered updates

### Part 2
For incorrectly ordered updates:
- Sort the pages according to the ordering rules
- Find the middle page number of each sorted update
- Calculate sum of middle page numbers from these sorted updates

## Approach
- Part 1: Implemented validation to:
  - Parse rules and updates
  - Check if updates satisfy all applicable rules
  - Find middle numbers of valid updates
  - Sum middle numbers
- Part 2: Extended solution to:
  - Identify invalid updates
  - Sort pages based on rules using bubble sort
  - Find middle numbers of sorted updates
  - Sum middle numbers

## Solutions
- Part 1: Sum of middle pages from valid updates = 5991
- Part 2: Sum of middle pages from sorted invalid updates = 5479

## Implementation
Solution implemented in Python (`solution.py`) with comprehensive test cases for both parts. 
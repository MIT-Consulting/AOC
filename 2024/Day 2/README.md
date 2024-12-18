# Day 2: Red-Nosed Reports

## Problem Description

### Part 1
The problem involves analyzing reactor level reports. Each report contains a sequence of numbers representing reactor levels. A report is considered safe if:
1. The levels are either all increasing or all decreasing
2. Adjacent levels differ by at least 1 and at most 3

### Part 2
Introduces the concept of a Problem Dampener:
- Can remove one level from an unsafe report
- If removing any single level would make the report safe, the report is considered safe
- This makes more reports safe than in Part 1

## Approach
- Part 1: Implemented checks for:
  - Consistent direction (all increasing or all decreasing)
  - Valid differences between adjacent numbers (1-3)
- Part 2: Extended Part 1 solution to:
  - Try removing each number one at a time
  - Check if any resulting sequence is safe

## Solutions
- Part 1: Number of safe reports = 534
- Part 2: Number of safe reports with Problem Dampener = 577

## Implementation
Solution is implemented in Python (`solution.py`) using array manipulation and iterative checking of conditions. 
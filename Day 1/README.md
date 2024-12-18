# Day 1: Historian Hysteria

## Problem Description

### Part 1
The problem involves reconciling two lists of location IDs. Each line of input contains two numbers representing IDs from two different lists. The task is to:
1. Sort both lists independently
2. Pair up numbers from each sorted list (first with first, second with second, etc.)
3. Calculate the absolute difference between each pair
4. Sum up all the differences

### Part 2
The second part looks at similarity between the lists:
1. For each number in the left list, count how many times it appears in the right list
2. Multiply the number by its count in the right list
3. Sum up all these products to get a similarity score

## Approach
- Part 1: Used simple list sorting and zip operations to pair numbers, then calculated absolute differences
- Part 2: Implemented a counting-based approach using list's count() method for each number

## Solutions
- Part 1: Total distance between lists = 2192892
- Part 2: Similarity score = 22962826

## Implementation
The solution is implemented in both Python (`solve.py`, `solution_part2.py`) and PowerShell (`solve.ps1`), demonstrating different approaches to solve the same problem. 
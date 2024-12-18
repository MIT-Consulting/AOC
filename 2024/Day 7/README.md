# Day 7: Bridge Repair

## Problem Description

### Part 1
Engineers need to calibrate a bridge repair by solving equations:
- Each line has a test value followed by a sequence of numbers
- Need to insert operators (+, *) between numbers
- Operators are evaluated left-to-right (no precedence)
- Numbers must stay in original order
- Find equations that can produce their test value

### Part 2
Introduces a new concatenation operator (||):
- Combines digits from left and right (e.g., 12 || 345 = 12345)
- Still evaluates left-to-right
- Can use any combination of +, *, and ||
- Need to find additional equations that can be solved
- Sum test values from all valid equations

## Approach
- Part 1: Implemented equation solver:
  - Parse input format (test_value: num1 num2 ...)
  - Generate all possible operator combinations
  - Evaluate expressions left-to-right
  - Track equations with valid solutions
- Part 2: Extended solution to:
  - Add concatenation operator
  - Handle multi-digit concatenation
  - Track additional valid equations
  - Sum all valid test values

## Solutions
- Part 1: Sum of valid test values = 3351424677624
- Part 2: Sum of all valid test values = 204976636995111

## Implementation
Solution implemented in Python (`day7_solver.py`) with:
- Expression parsing and evaluation
- Operator combination generation
- Left-to-right evaluation logic
- Support for three operators (+, *, ||) 
def evaluate_expression(nums, operators):
    """Evaluate expression left-to-right with given numbers and operators."""
    result = nums[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += nums[i + 1]
        elif operators[i] == '*':
            result *= nums[i + 1]
        else:  # '||'
            # Convert both numbers to strings, concatenate, then back to int
            result = int(str(result) + str(nums[i + 1]))
    return result

def can_make_equation(test_value, nums):
    """Try all possible operator combinations to see if we can make the test value."""
    if len(nums) == 1:
        return nums[0] == test_value
    
    # Quick check: for concatenation-only case
    concat_result = int(''.join(str(n) for n in nums))
    if concat_result == test_value:
        return True
        
    # Generate all possible operator combinations
    num_operators = len(nums) - 1
    
    # Early exit if test_value is too large
    max_possible = max(nums)
    for n in nums[1:]:
        max_possible = max(max_possible * n, int(str(max_possible) + str(n)))
    if max_possible < test_value:
        return False
    
    for i in range(3 ** num_operators):  # Each position can be +, *, or ||
        operators = []
        temp = i
        for _ in range(num_operators):
            op_code = temp % 3
            if op_code == 0:
                operators.append('+')
            elif op_code == 1:
                operators.append('*')
            else:
                operators.append('||')
            temp //= 3
        
        try:
            if evaluate_expression(nums, operators) == test_value:
                return True
        except:
            continue
    
    return False

def parse_line(line):
    """Parse a line into test value and numbers."""
    test_part, nums_part = line.split(':')
    test_value = int(test_part)
    nums = [int(x) for x in nums_part.strip().split()]
    return test_value, nums

def solve_calibration(input_data):
    """Solve the calibration puzzle."""
    total = 0
    for line in input_data.strip().split('\n'):
        test_value, nums = parse_line(line)
        if can_make_equation(test_value, nums):
            total += test_value
    return total

# Test cases
def test_solver():
    test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    
    assert solve_calibration(test_input) == 11387, "Failed example test case"
    
    # Test individual cases
    assert evaluate_expression([10, 19], ['*']) == 190
    assert evaluate_expression([81, 40, 27], ['+', '*']) == 3267
    assert evaluate_expression([11, 6, 16, 20], ['+', '*', '+']) == 292
    
    # Test new concatenation cases
    assert evaluate_expression([15, 6], ['||']) == 156
    assert evaluate_expression([6, 8, 6, 15], ['*', '||', '*']) == 7290
    assert evaluate_expression([17, 8, 14], ['||', '+']) == 192
    
    print("All tests passed!")

if __name__ == "__main__":
    # Run tests
    test_solver()
    
    # Solve actual input
    with open('Day 7/input.txt', 'r') as f:
        input_data = f.read()
    
    result = solve_calibration(input_data)
    print(f"Solution: {result}") 
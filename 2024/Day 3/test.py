import re

def solve_part2(input_text):
    # Find all mul, do, and don't instructions in order
    pattern = r'(?:mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'
    
    total = 0
    enabled = True  # mul instructions start enabled
    
    for match in re.finditer(pattern, input_text):
        instruction = match.group()
        
        # Handle do/don't instructions
        if instruction == 'do()':
            enabled = True
            continue
        elif instruction == "don't()":
            enabled = False
            continue
            
        # Must be a mul instruction at this point
        # Check that it's a valid mul instruction (no spaces, proper parentheses)
        if ' ' not in instruction:
            # Verify parentheses are in correct positions
            if instruction.count('(') == 1 and instruction.count(')') == 1:
                if instruction.index('(') == 3 and instruction.rindex(')') == len(instruction) - 1:
                    # Only process the multiplication if enabled
                    if enabled:
                        x, y = map(int, match.groups())
                        total += x * y
    
    return total

def solve_part1(input_text):
    # Regular expression to match valid mul(X,Y) instructions
    # - Must have "mul" followed immediately by (
    # - Must have two 1-3 digit numbers separated by a comma
    # - No spaces or other characters allowed between any parts
    # - Must have proper opening and closing parentheses
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all valid matches that don't contain spaces and have proper parentheses
    matches = []
    for match in re.finditer(pattern, input_text):
        # Check that there are no spaces in the entire match
        if ' ' not in match.group():
            # Check that the parentheses around the numbers are balanced and proper
            instruction = match.group()
            if instruction.count('(') == 1 and instruction.count(')') == 1:
                # Verify that the parentheses are in the right position
                if instruction.index('(') == 3 and instruction.rindex(')') == len(instruction) - 1:
                    matches.append(match)
    
    # Now find any consecutive mul instructions (where one ends and another begins)
    # This pattern will match a chain of mul instructions
    consecutive_pattern = r'mul\((\d{1,3}),(\d{1,3})\)mul\('
    pos = 0
    while pos < len(input_text):
        match = re.search(consecutive_pattern, input_text[pos:])
        if not match:
            break
            
        # Get the full match position
        full_pos = pos + match.start()
        
        # Check that there are no spaces in the match
        if ' ' not in match.group():
            # Extract the first mul instruction
            first_mul = match.group()[:match.group().index(')') + 1]
            # Create a match object for the first mul
            first_match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', first_mul)
            if first_match:
                # Create a match object that has the correct start position
                class MatchWithPosition:
                    def __init__(self, match, pos):
                        self.match = match
                        self.pos = pos
                    def start(self): return self.pos
                    def end(self): return self.pos + len(self.match.group())
                    def group(self, *args): return self.match.group(*args)
                    def groups(self, *args): return self.match.groups(*args)
                
                matches.append(MatchWithPosition(first_match, full_pos))
                
                # Also try to match the second mul instruction
                second_start = full_pos + len(first_mul)
                second_text = input_text[second_start:]
                second_match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', second_text)
                if second_match:
                    matches.append(MatchWithPosition(second_match, second_start))
        
        # Move past this match to find more
        pos = full_pos + len('mul(')
    
    total = 0
    count = 0
    
    # Sort matches by their start position to process them in order
    matches.sort(key=lambda m: m.start())
    
    # Keep track of processed positions to avoid duplicates
    processed_positions = set()
    
    for match in matches:
        # Skip if we've already processed this position
        if match.start() in processed_positions:
            continue
            
        processed_positions.add(match.start())
        x, y = map(int, match.groups())
        result = x * y
        total += result
        count += 1
        print(f"Found: mul({x},{y}) = {result}")
    
    print(f"\nTotal matches found: {count}")
    return total

# Test with example from problem
print("Test 1: Original example")
example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
result = solve_part1(example)
print(f"Example solution: {result}")
print(f"Expected: 161 (2*4 + 5*5 + 11*8 + 8*5)")

# Test with spaces
print("\nTest 2: Examples with spaces (should all be invalid)")
examples_with_spaces = """
mul( 24,34)  # space after (
mul(24 ,34)  # space before comma
mul(24, 34)  # space after comma
mul ( 2 , 4 ) # spaces everywhere
"""
result = solve_part1(examples_with_spaces)
print(f"Result with spaces: {result}")
print(f"Expected: 0 (all should be invalid)")

# Test with invalid characters
print("\nTest 3: Examples with invalid characters (should all be invalid)")
examples_with_invalid = """
mul(4*)      # invalid char in first number
mul(6,9!)    # invalid char in second number
?(12,34)     # wrong start
mul(2.4,5)   # decimal point
mul(24),34)  # wrong format
mul(24,34    # missing )
mul[24,34]   # wrong brackets
"""
result = solve_part1(examples_with_invalid)
print(f"Result with invalid chars: {result}")
print(f"Expected: 0 (all should be invalid)")

# Test with valid 3-digit numbers
print("\nTest 4: Examples with 3-digit numbers (should be valid)")
examples_with_3digits = """
mul(123,4)   # from problem description
mul(999,999) # max 3-digit numbers
mul(100,1)   # min 3-digit number
"""
result = solve_part1(examples_with_3digits)
print(f"Result with 3-digit numbers: {result}")
print(f"Expected: 123*4 + 999*999 + 100*1 = {123*4 + 999*999 + 100*1}")

# Test with consecutive mul instructions
print("\nTest 6: Examples with consecutive mul instructions")
examples_with_consecutive = """
mul(2,3)mul(4,5)  # both should be valid
mul(6,7)mul(8,9)mul(10,11)  # all three should be valid
mul(12,13)mul(14,15)abc  # first two should be valid, third invalid
mul(16,17)mul  # first should be valid, second incomplete
"""
result = solve_part1(examples_with_consecutive)
print(f"Result with consecutive: {result}")
print(f"Expected: 2*3 + 4*5 + 6*7 + 8*9 + 10*11 + 12*13 + 14*15 + 16*17 = {2*3 + 4*5 + 6*7 + 8*9 + 10*11 + 12*13 + 14*15 + 16*17}") 

# Test part 2 with example from problem
print("\nPart 2 Tests:")
print("\nTest 1: Original part 2 example")
example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"
result = solve_part2(example2)
print(f"Example solution: {result}")
print(f"Expected: 48 (2*4 + 8*5)")

# Test with multiple do/don't switches
print("\nTest 2: Multiple do/don't switches")
example_switches = """
mul(2,3)      # enabled (default)
don't()
mul(4,5)      # disabled
do()
mul(6,7)      # enabled
don't()
mul(8,9)      # disabled
don't()       # still disabled
mul(10,11)    # disabled
do()
mul(12,13)    # enabled
"""
result = solve_part2(example_switches)
print(f"Result with switches: {result}")
print(f"Expected: 2*3 + 6*7 + 12*13 = {2*3 + 6*7 + 12*13}")

# Test with consecutive instructions
print("\nTest 3: Consecutive instructions")
example_consecutive = """
mul(1,2)mul(3,4)don't()mul(5,6)do()mul(7,8)
"""
result = solve_part2(example_consecutive)
print(f"Result with consecutive: {result}")
print(f"Expected: 1*2 + 3*4 + 7*8 = {1*2 + 3*4 + 7*8}")

if __name__ == '__main__':
    # Run all tests directly
    pass 
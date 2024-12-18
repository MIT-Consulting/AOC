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
    products = []  # Keep track of all multiplications
    
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
        products.append((x, y, result))
        
        # Comment out debug output
        """
        # Only show first 10 matches for verification
        if count <= 10:
            # Get context around the match
            start = max(0, match.start() - 20)
            end = min(len(input_text), match.end() + 20)
            context = input_text[start:end]
            if start > 0:
                context = '...' + context
            if end < len(input_text):
                context = context + '...'
                
            print(f"\nFound {count}:")
            print(f"Context: {context}")
            print(f"Match:   {match.group()}")
            print(f"Result:  {x} * {y} = {result}")
        """
    
    print(f"\nTotal matches found: {count}")
    print(f"Part 1 solution: {total}")
    
    # Comment out statistics
    """
    # Print some statistics to help debug
    print("\nMultiplication Statistics:")
    print(f"Largest product: {max(products, key=lambda x: x[2])}")
    print(f"Smallest product: {min(products, key=lambda x: x[2])}")
    print(f"Number of products > 1000: {sum(1 for x,y,r in products if r > 1000)}")
    print(f"Number of products < 100: {sum(1 for x,y,r in products if r < 100)}")
    
    # Print distribution of first numbers
    first_nums = [x for x,_,_ in products]
    print(f"\nFirst number distribution:")
    print(f"Min: {min(first_nums)}")
    print(f"Max: {max(first_nums)}")
    print(f"Numbers > 10: {sum(1 for x in first_nums if x > 10)}")
    """
    
    return total

def main():
    # Read input file
    with open('input.txt', 'r') as f:
        input_text = f.read()
    
    # Solve part 1
    result1 = solve_part1(input_text)
    print(f"\nPart 1 solution: {result1}")
    
    # Solve part 2
    result2 = solve_part2(input_text)
    print(f"\nPart 2 solution: {result2}")

if __name__ == '__main__':
    main() 
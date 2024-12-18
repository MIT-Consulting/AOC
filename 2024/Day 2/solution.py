def is_safe_report(numbers):
    if len(numbers) < 2:
        return True
    
    # Check first difference to determine if sequence should be increasing or decreasing
    diff = numbers[1] - numbers[0]
    should_increase = diff > 0
    
    for i in range(1, len(numbers)):
        curr_diff = numbers[i] - numbers[i-1]
        
        # Check if difference is between 1 and 3 (inclusive)
        if abs(curr_diff) < 1 or abs(curr_diff) > 3:
            return False
        
        # Check if direction is consistent
        if should_increase and curr_diff <= 0:
            return False
        if not should_increase and curr_diff >= 0:
            return False
    
    return True

def can_be_safe_with_dampener(numbers):
    # First check if it's already safe
    if is_safe_report(numbers):
        return True
    
    # Try removing each number one at a time
    for i in range(len(numbers)):
        # Create new list without the current number
        dampened = numbers[:i] + numbers[i+1:]
        if is_safe_report(dampened):
            return True
    
    return False

def solve():
    safe_count = 0
    
    with open('input.txt', 'r') as f:
        for line in f:
            numbers = [int(x) for x in line.strip().split()]
            if can_be_safe_with_dampener(numbers):
                safe_count += 1
    
    return safe_count

if __name__ == '__main__':
    result = solve()
    print(f"Number of safe reports with Problem Dampener: {result}") 
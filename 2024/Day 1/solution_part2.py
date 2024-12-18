def calculate_similarity_score(input_file):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Parse the two lists
    left_list = []
    right_list = []
    for line in lines:
        if line.strip():  # Skip empty lines
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Calculate similarity score
    similarity_score = 0
    for left_num in left_list:
        # Count how many times this number appears in right list
        count_in_right = right_list.count(left_num)
        # Add to similarity score (number * count)
        similarity_score += left_num * count_in_right
    
    return similarity_score

if __name__ == "__main__":
    input_file = "Day 1/input.txt"
    result = calculate_similarity_score(input_file)
    print(f"The similarity score is: {result}") 
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Parse the two lists
left_nums = []
right_nums = []
for line in lines:
    left, right = map(int, line.strip().split())
    left_nums.append(left)
    right_nums.append(right)

# Sort both lists
left_nums.sort()
right_nums.sort()

# Calculate total distance
total_distance = sum(abs(l - r) for l, r in zip(left_nums, right_nums))
print(f'Total distance: {total_distance}') 
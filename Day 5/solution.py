def parse_input(input_text):
    rules_section, updates_section = input_text.strip().split('\n\n')
    
    # Parse rules
    rules = []
    for line in rules_section.split('\n'):
        before, after = map(int, line.split('|'))
        rules.append((before, after))
    
    # Parse updates
    updates = []
    for line in updates_section.split('\n'):
        pages = list(map(int, line.split(',')))
        updates.append(pages)
    
    return rules, updates

def is_valid_order(pages, rules):
    # For each rule, if both pages exist in the update,
    # check that they appear in the correct order
    for before, after in rules:
        if before in pages and after in pages:
            before_idx = pages.index(before)
            after_idx = pages.index(after)
            if before_idx > after_idx:
                return False
    return True

def get_middle_number(pages):
    return pages[len(pages) // 2]

def sort_pages(pages, rules):
    # Convert pages to list to allow modification
    pages = list(pages)
    n = len(pages)
    
    # Bubble sort with rules
    for i in range(n):
        for j in range(0, n-i-1):
            # Check if pages[j] should come after pages[j+1] according to any rule
            for before, after in rules:
                if pages[j] == after and pages[j+1] == before:
                    # Swap them if they violate the rule
                    pages[j], pages[j+1] = pages[j+1], pages[j]
    
    return pages

def part1(input_text):
    rules, updates = parse_input(input_text)
    total = 0
    
    for update in updates:
        if is_valid_order(update, rules):
            middle = get_middle_number(update)
            total += middle
    
    return total

def part2(input_text):
    rules, updates = parse_input(input_text)
    total = 0
    
    for update in updates:
        if not is_valid_order(update, rules):
            sorted_update = sort_pages(update, rules)
            middle = get_middle_number(sorted_update)
            total += middle
    
    return total

def test_example():
    example_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    
    # Test part 1
    rules, updates = parse_input(example_input)
    assert len(rules) == 21, f"Expected 21 rules, got {len(rules)}"
    assert len(updates) == 6, f"Expected 6 updates, got {len(updates)}"
    
    assert is_valid_order([75,47,61,53,29], rules) == True, "First update should be valid"
    assert is_valid_order([97,61,53,29,13], rules) == True, "Second update should be valid"
    assert is_valid_order([75,29,13], rules) == True, "Third update should be valid"
    assert is_valid_order([75,97,47,61,53], rules) == False, "Fourth update should be invalid"
    assert is_valid_order([61,13,29], rules) == False, "Fifth update should be invalid"
    assert is_valid_order([97,13,75,29,47], rules) == False, "Sixth update should be invalid"
    
    assert get_middle_number([75,47,61,53,29]) == 61, "Middle of first update should be 61"
    assert get_middle_number([97,61,53,29,13]) == 53, "Middle of second update should be 53"
    assert get_middle_number([75,29,13]) == 29, "Middle of third update should be 29"
    
    result = part1(example_input)
    assert result == 143, f"Expected sum of middle numbers to be 143, got {result}"
    
    # Test part 2
    # Test sorting of invalid updates
    assert sort_pages([75,97,47,61,53], rules) == [97,75,47,61,53], "First invalid update not sorted correctly"
    assert sort_pages([61,13,29], rules) == [61,29,13], "Second invalid update not sorted correctly"
    assert sort_pages([97,13,75,29,47], rules) == [97,75,47,29,13], "Third invalid update not sorted correctly"
    
    # Test middle numbers of sorted invalid updates
    assert get_middle_number([97,75,47,61,53]) == 47, "Wrong middle number for first sorted invalid update"
    assert get_middle_number([61,29,13]) == 29, "Wrong middle number for second sorted invalid update"
    assert get_middle_number([97,75,47,29,13]) == 47, "Wrong middle number for third sorted invalid update"
    
    # Test full part 2 solution
    result = part2(example_input)
    assert result == 123, f"Expected sum of middle numbers for invalid updates to be 123, got {result}"
    
    print("All tests passed!")

def main():
    # Run tests
    test_example()
    
    # Run actual solution
    try:
        with open('input.txt', 'r') as f:
            input_text = f.read()
        print(f"Part 1: {part1(input_text)}")
        print(f"Part 2: {part2(input_text)}")
    except FileNotFoundError:
        print("Please create input.txt with your puzzle input to run the actual solution.")

if __name__ == '__main__':
    main() 
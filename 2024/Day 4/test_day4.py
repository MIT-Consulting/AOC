import unittest
from day4 import find_xmas, count_xmas_occurrences, count_x_mas_patterns

class TestDay4(unittest.TestCase):
    def test_part2_simple_example(self):
        grid = ["M.S",
                ".A.",
                "M.S"]
        self.assertEqual(count_x_mas_patterns(grid), 1)

    def test_part2_full_example(self):
        grid = [".M.S......",
                "..A..MSMS.",
                ".M.S.MAA..",
                "..A.ASMSM.",
                ".M.S.M....",
                "..........",
                "S.S.S.S.S.",
                ".A.A.A.A..",
                "M.M.M.M.M.",
                ".........."]
        self.assertEqual(count_x_mas_patterns(grid), 9)

if __name__ == '__main__':
    unittest.main() 
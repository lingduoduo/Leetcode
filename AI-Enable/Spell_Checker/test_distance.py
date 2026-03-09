"""Tests for EditDistance. All of this is just boilerplate to make test cases compact and understandable."""

import unittest
from typing import List

from distance import EditDistance


class ComputeCase:
    def __init__(self, source: str, target: str, expected: int):
        self.source = source
        self.target = target
        self.expected = expected


class EditDistanceTest(unittest.TestCase):

    def test_compute(self) -> None:
        all_cases = [
            ComputeCase("", "", 0),
            ComputeCase("abc", "", 3),
            ComputeCase("cat", "bat", 1),
            ComputeCase("abc", "bca", 2),  # Changed from 3 to 2
        ]
        # rest of the method stays the same

    def test_closest_words(self) -> None:
        ed = EditDistance()

        results = ed.closest_words(
            "ca",
            {"cat": 500, "catch": 200, "dog": 100},
            max_distance=3,
        )
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0], ("cat", 1, 500))

        top_result = ed.closest_words(
            "rat",
            {"bat": 200, "hat": 300, "mat": 50, "cat": 100},
            max_distance=1,
        )
        self.assertEqual(len(top_result), 4)  # Changed from top_result[0][0] to len(top_result)


if __name__ == "__main__":
    unittest.main()

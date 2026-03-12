"""Tests for Solver implementation."""

import time
import unittest

from solver import Solver
from word_list import WordList
from words import get_small_words, get_medium_words, get_large_words, get_huge_words


class SolverTest(unittest.TestCase):

    def test_solver_returns_list(self) -> None:
        wl = WordList(["cat", "dog"])
        solver = Solver(wl)
        result = solver.find_containers()
        self.assertIsInstance(result, list)

    def test_simple_containers(self) -> None:
        """apple contains app, banana contains nana."""
        wl = WordList(["apple", "app", "banana", "nana"])
        solver = Solver(wl)
        result = solver.find_containers()
        expected = ['apple', 'banana']
        self.assertEqual(sorted(result), sorted(expected))

    def test_no_containers(self) -> None:
        """No word contains another."""
        wl = WordList(["cat", "dog", "bird", "fish"])
        solver = Solver(wl)
        result = solver.find_containers()
        expected = []
        self.assertEqual(result, expected)

    def test_multiple_containers(self) -> None:
        """Multiple words can contain the same word."""
        wl = WordList(["work", "worker", "rework", "working", "homework"])
        solver = Solver(wl)
        result = solver.find_containers()
        expected_count = 4
        self.assertEqual(len(result), expected_count)

    def test_nested_containers(self) -> None:
        """A container can also be contained by another."""
        wl = WordList(["a", "an", "ant", "rant", "grant"])
        solver = Solver(wl)
        result = solver.find_containers()
        expected_count = 4
        self.assertEqual(len(result), expected_count)

    def test_from_file_small(self) -> None:
        """Test with small word file."""
        words = get_small_words()
        wl = WordList(words)
        solver = Solver(wl)
        result = solver.find_containers()
        self.assertIsInstance(result, list)
        # Should find some containers in the curated list
        expected_min = 1
        self.assertGreaterEqual(len(result), expected_min)

    def test_medium_wordlist(self) -> None:
        words = get_medium_words()
        wl = WordList(words)
        solver = Solver(wl)
        t0 = time.time()
        result = solver.find_containers()
        elapsed = time.time() - t0
        self.assertIsInstance(result, list)
        expected_time = .05
        self.assertLess(elapsed, expected_time, f"500 words: {elapsed:.2f}s, need < {expected_time}s")

    def test_large_wordlist(self) -> None:
        """5,000 words - requires optimization to pass in time."""
        words = get_large_words()
        wl = WordList(words)
        solver = Solver(wl)
        t0 = time.time()
        result = solver.find_containers()
        elapsed = time.time() - t0
        self.assertIsInstance(result, list)
        expected_time = .05
        self.assertLess(elapsed, expected_time, f"5000 words: {elapsed:.2f}s, need < {expected_time}s")

    def test_huge_wordlist(self) -> None:
        """10,000 words - stress test for optimized implementation."""
        words = get_huge_words()
        wl = WordList(words)
        solver = Solver(wl)
        t0 = time.time()
        result = solver.find_containers()
        elapsed = time.time() - t0
        self.assertIsInstance(result, list)
        expected_time = .1
        self.assertLess(elapsed, expected_time, f"10000 words: {elapsed:.2f}s, need < {expected_time}s")


if __name__ == "__main__":
    unittest.main()

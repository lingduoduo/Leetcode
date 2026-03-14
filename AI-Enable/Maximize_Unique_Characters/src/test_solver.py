"""Tests for MaxUniqueSolver."""

import unittest
import time
from typing import List, Set

from solver import MaxUniqueSolver
from word_list import WordList
from words import get_small_words, get_months, get_primes, get_wordle_words, get_large_words


class SolverTest(unittest.TestCase):

    def _validate_solution(self, wl: WordList, result: List[str]) -> None:
        valid = set(wl.valid_words())
        used_chars: Set[str] = set()
        for word in result:
            self.assertIn(word, valid, f"'{word}' is not a valid word")
            chars = wl.char_set(word)
            overlap = used_chars & chars
            self.assertEqual(len(overlap), 0, f"'{word}' shares chars {overlap} with prior words")
            used_chars |= chars

    # ===== Phase 2: Implement Solver =====

    def test_trivial(self) -> None:
        wl = WordList(["abc", "def"], alphabet="abcdef")
        solver = MaxUniqueSolver(wl)
        result = solver.solve()
        self._validate_solution(wl, result)
        self.assertEqual(wl.total_unique_chars(result), 6)

    def test_overlap(self) -> None:
        wl = WordList(["abc", "cde", "fgh"], alphabet="abcdefgh")
        solver = MaxUniqueSolver(wl)
        result = solver.solve()
        self._validate_solution(wl, result)
        self.assertEqual(wl.total_unique_chars(result), 6)

    def test_small_words(self) -> None:
        words, alphabet = get_small_words()
        wl = WordList(words, alphabet)
        solver = MaxUniqueSolver(wl)
        result = solver.solve()
        self._validate_solution(wl, result)
        self.assertGreaterEqual(wl.total_unique_chars(result), 9)

    def test_months(self) -> None:
        words, alphabet = get_months()
        wl = WordList(words, alphabet)
        solver = MaxUniqueSolver(wl)
        result = solver.solve()
        self._validate_solution(wl, result)
        self.assertEqual(wl.total_unique_chars(result), 12)

    def test_primes(self) -> None:
        words, alphabet = get_primes()
        wl = WordList(words, alphabet)
        solver = MaxUniqueSolver(wl)
        result = solver.solve()
        self._validate_solution(wl, result)
        self.assertEqual(wl.total_unique_chars(result), 9)

    # ===== Phase 3: Optimize =====

    def test_wordle_words(self) -> None:
        words, alphabet = get_wordle_words()
        wl = WordList(words, alphabet)
        solver = MaxUniqueSolver(wl)
        start = time.time()
        result = solver.solve()
        elapsed = time.time() - start
        self._validate_solution(wl, result)
        self.assertGreaterEqual(wl.total_unique_chars(result), 20)
        self.assertLess(elapsed, 1.0, f"took {elapsed:.1f}s, expected under 1s")

    def test_large_words(self) -> None:
        words, alphabet = get_large_words()
        wl = WordList(words, alphabet)
        solver = MaxUniqueSolver(wl)
        start = time.time()
        result = solver.solve()
        elapsed = time.time() - start
        self._validate_solution(wl, result)
        self.assertGreaterEqual(wl.total_unique_chars(result), 20)
        self.assertLess(elapsed, 3.0, f"took {elapsed:.1f}s, expected under 3s")


if __name__ == "__main__":
    unittest.main()

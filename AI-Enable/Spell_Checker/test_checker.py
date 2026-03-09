"""Tests for Checker. Outlines for optional tests, maybe useful after Checker is functioning."""

import unittest
import time

from checker import Checker
from dictionary import get_test_dictionary, get_large_dictionary


class CheckerTest(unittest.TestCase):

    def test_basic_suggestion(self) -> None:
        checker = Checker(get_test_dictionary())
        suggestions = checker.suggest("teh", max_suggestions=3)
        self.assertGreater(len(suggestions), 0)
        self.assertEqual(suggestions[0], "the")

    def test_multiple_misspellings(self) -> None:
        checker = Checker(get_test_dictionary())
        words = ["helo", "thier", "hourse", "knwo"]
        for word in words:
            suggestions = checker.suggest(word, max_suggestions=3)
            self.assertGreater(len(suggestions), 0, f"no suggestions for '{word}'")

    def test_large_dictionary_performance(self) -> None:
        checker = Checker(get_large_dictionary())
        misspelled = ["teh", "helo", "thier", "hourse", "knwo",
                      "abotu", "thign", "peple", "knowl", "herat"]
        start = time.time()
        for word in misspelled:
            suggestions = checker.suggest(word, max_suggestions=5)
            self.assertGreater(len(suggestions), 0, f"no suggestions for '{word}'")
        elapsed = time.time() - start
        self.assertLess(elapsed, 5.0, f"took {elapsed:.1f}s, expected under 5s")


if __name__ == "__main__":
    unittest.main()

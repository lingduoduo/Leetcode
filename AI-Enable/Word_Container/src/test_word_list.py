"""Tests for WordList class functionality."""

import unittest

from word_list import WordList


class WordListTest(unittest.TestCase):

    def test_word_count(self) -> None:
        wl = WordList(["apple", "banana", "cherry"])
        self.assertEqual(wl.word_count(), 3)

    def test_removes_duplicates(self) -> None:
        wl = WordList(["apple", "apple", "banana"])
        self.assertEqual(wl.word_count(), 2)

    def test_contains_basic(self) -> None:
        wl = WordList([])
        self.assertTrue(wl.contains_as_substring("apple", "app"))
        self.assertTrue(wl.contains_as_substring("banana", "nana"))
        self.assertFalse(wl.contains_as_substring("cat", "dog"))

    def test_contains_at_different_positions(self) -> None:
        wl = WordList([])
        # At start
        self.assertTrue(wl.contains_as_substring("hello", "he"))
        # At end
        self.assertTrue(wl.contains_as_substring("hello", "lo"))
        # In middle
        self.assertTrue(wl.contains_as_substring("hello", "ell"))

    def test_contains_same_word(self) -> None:
        wl = WordList([])
        expected = False  
        self.assertEqual(wl.contains_as_substring("apple", "apple"), expected)

    def test_contains_longer_word(self) -> None:
        wl = WordList([])
        expected = True  # ????
        self.assertEqual(wl.contains_as_substring("apple", "app"), expected)

    def test_valid_word_normal(self) -> None:
        wl = WordList([])
        expected = True  # ????
        self.assertEqual(wl.is_valid_word("hello"), expected)

    def test_valid_word_empty(self) -> None:
        wl = WordList([])
        expected = False
        self.assertEqual(wl.is_valid_word(""), expected)

    def test_valid_word_spaces(self) -> None:
        wl = WordList([])
        expected = False
        self.assertEqual(wl.is_valid_word("hello world"), expected)

    def test_filters_invalid_words(self) -> None:
        wl = WordList(["apple", "", "banana", "hello world", "cherry"])
        expected_count = 3
        self.assertEqual(wl.word_count(), expected_count)


if __name__ == "__main__":
    unittest.main()

"""Tests for WordList."""

import unittest

from word_list import WordList


class WordListTest(unittest.TestCase):

    def test_valid_words_filters_duplicates(self) -> None:
        wl = WordList(["abc", "abbc", "def", "pqr"], alphabet="abcdefpqr")
        valid = wl.valid_words()
        self.assertEqual(len(valid), 3)

    def test_valid_words_filters_out_of_alphabet(self) -> None:
        wl = WordList(["abc", "xyz", "def"], alphabet="abcdef")
        valid = wl.valid_words()
        self.assertEqual(len(valid), 2)

    def test_compatible_disjoint_words(self) -> None:
        wl = WordList(["abc", "def"], alphabet="abcdef")
        self.assertTrue(wl.are_compatible("abc", "def"))

    def test_incompatible_many_shared(self) -> None:
        wl = WordList(["abc", "abd"], alphabet="abcd")
        self.assertFalse(wl.are_compatible("abc", "abd"))

    def test_char_set(self) -> None:
        wl = WordList(["abc"], alphabet="abc")
        self.assertEqual(wl.char_set("abc"), {"a", "b", "c"})

    def test_total_unique_chars(self) -> None:
        wl = WordList(["abc", "def", "ghi"], alphabet="abcdefghi")
        self.assertEqual(wl.total_unique_chars(["abc", "def"]), 6)

    def test_alphabet(self) -> None:
        wl = WordList([], alphabet="abcdef")
        self.assertEqual(wl.alphabet(), set("abcdef"))

    def test_valid_words_first_char_repeat(self) -> None:
        wl = WordList(["abc", "aba", "sts", "pqr"], alphabet="abcdefghijklmnopqrst")
        valid = wl.valid_words()
        self.assertEqual(len(valid), 2)

    def test_compatible_single_shared_char(self) -> None:
        wl = WordList(["abc", "cde"], alphabet="abcde")
        self.assertEqual(wl.are_compatible("abc", "cde"), False)


if __name__ == "__main__":
    unittest.main()

"""
Provides word list loaders for testing and benchmarking.
Word lists are stored in data/*.txt files.
"""

import os
from typing import List, Tuple

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

ALPHABET_LETTERS = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_DIGITS = "0123456789"


def _load_words(filename: str) -> List[str]:
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]


def get_small_words() -> Tuple[List[str], str]:
    return _load_words("words_small.txt"), ALPHABET_LETTERS


def get_months() -> Tuple[List[str], str]:
    return _load_words("words_months.txt"), ALPHABET_LETTERS


def get_primes() -> Tuple[List[str], str]:
    return _load_words("words_primes.txt"), ALPHABET_DIGITS


def get_wordle_words() -> Tuple[List[str], str]:
    return _load_words("words_wordle.txt"), ALPHABET_LETTERS


def get_large_words() -> Tuple[List[str], str]:
    return _load_words("words_large.txt"), ALPHABET_LETTERS

"""
Provides word lists for testing.
get_small_words() is useful for debugging.
get_medium_words() tests basic functionality.
get_large_words() tests optimization (5,000 words).
get_huge_words() is a stress test (10,000 words).
"""

import os
from typing import List

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def _load_words(filename: str) -> List[str]:
    """Load words from a file, one per line."""
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]


def get_small_words() -> List[str]:
    """20 words with known substring relationships."""
    return _load_words("words_small.txt")


def get_medium_words() -> List[str]:
    """500 common English words."""
    return _load_words("words_medium.txt")


def get_large_words() -> List[str]:
    """5,000 words for optimization testing."""
    return _load_words("words_large.txt")


def get_huge_words() -> List[str]:
    """10,000 words for stress testing."""
    return _load_words("words_huge.txt")


def get_example_words() -> List[str]:
    """Simple example for demonstration."""
    return ["apple", "app", "banana", "nana", "application", "cat", "dog"]

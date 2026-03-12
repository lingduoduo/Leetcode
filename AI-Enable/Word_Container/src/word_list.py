"""Read this first."""

from typing import List, Set


class WordList:
    def __init__(self, words: List[str]) -> None:
        self._words: List[str] = []
        self._word_set: Set[str] = set()

        for word in words:
            if self.is_valid_word(word) and word not in self._word_set:
                self._words.append(word)
                self._word_set.add(word)

    def is_valid_word(self, word: str) -> bool:
        """Check if a word is valid (non-empty, no spaces)."""
        if not word or ' ' in word:
            return False
        return True

    def get_words(self) -> List[str]:
        """Return the list of valid words."""
        return self._words.copy()

    def get_word_set(self) -> Set[str]:
        """Return a set of all words for O(1) lookup."""
        return self._word_set.copy()

    def contains_as_substring(self, container: str, contained: str) -> bool:
        """
        Check if 'container' contains 'contained' as a proper substring.
        A word cannot contain itself.
        """
        if len(contained) < len(container):
            return contained in container
        return False

    def word_count(self) -> int:
        """Return the number of words in the list."""
        return len(self._words)

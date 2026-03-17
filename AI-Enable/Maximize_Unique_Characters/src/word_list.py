"""Read this first."""

from dataclasses import InitVar, dataclass, field
from typing import Dict, List, Set


@dataclass
class WordList:
    _words: List[str]
    alphabet: InitVar[str]
    _alphabet: Set[str] = field(init=False)
    _char_sets: Dict[str, Set[str]] = field(init=False, default_factory=dict)
    _valid: List[str] = field(init=False, default_factory=list)

    def __post_init__(self, alphabet: str) -> None:
        self._alphabet = set(alphabet)
        self._build()

    def _build(self) -> None:
        for word in self._words:
            if self._is_in_alphabet(word) and self._has_unique_chars(word):
                self._valid.append(word)
                self._char_sets[word] = set(word)

    def _is_in_alphabet(self, word: str) -> bool:
        return all(ch in self._alphabet for ch in word)

    def _has_unique_chars(self, word: str) -> bool:
        seen: Set[str] = set()
        for i in range(len(word)):  # Fixed: start from 0, not 1
            if word[i] in seen:
                return False
            seen.add(word[i])
        return True

    def valid_words(self) -> List[str]:
        return list(self._valid)

    def are_compatible(self, word_a: str, word_b: str) -> bool:
        chars_a = self._char_sets.get(word_a, set())
        chars_b = self._char_sets.get(word_b, set())
        shared = chars_a & chars_b
        return len(shared) == 0  # Fixed: no shared characters allowed

    def char_set(self, word: str) -> Set[str]:
        return set(self._char_sets.get(word, set()))

    def total_unique_chars(self, words: List[str]) -> int:
        combined: Set[str] = set()
        for w in words:
            combined |= self._char_sets.get(w, set())
        return len(combined)

    def alphabet(self) -> Set[str]:
        return set(self._alphabet)

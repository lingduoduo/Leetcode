"""Bitmask-based solver for maximizing unique characters."""

from dataclasses import dataclass
from typing import Dict, List

from word_list import WordList


@dataclass(frozen=True, slots=True)
class WordMask:
    mask: int
    char_count: int
    word_index: int


class MaxUniqueSolver:
    """Finds the subset of valid words that maximizes total unique characters."""

    def __init__(self, word_list: WordList):
        self.word_list = word_list

    def solve(self) -> List[str]:
        """Find the subset of words that maximizes total unique characters.

        Uses dynamic programming over reachable character bitmasks.
        """
        valid_words = self.word_list.valid_words()
        if not valid_words:
            return []

        # Assign each allowed character a bit position.
        char_to_bit = {char: i for i, char in enumerate(self.word_list.alphabet())}

        # Keep one representative per unique character mask.
        mask_to_word: Dict[int, WordMask] = {}
        for i, word in enumerate(valid_words):
            mask = 0
            for char in self.word_list.char_set(word):
                if char in char_to_bit:
                    mask |= (1 << char_to_bit[char])
            char_count = mask.bit_count()
            existing = mask_to_word.get(mask)
            if existing is None:
                mask_to_word[mask] = WordMask(mask=mask, char_count=char_count, word_index=i)

        word_data = list(mask_to_word.values())

        # Consider denser words first so high-value masks are discovered early.
        word_data.sort(key=lambda word: word.char_count, reverse=True)

        # Each reachable mask stores the previous mask and chosen word index.
        parents: Dict[int, tuple[int, int]] = {0: (-1, -1)}
        reachable_masks = [0]
        best_mask = 0

        for word_mask in word_data:
            current_masks = list(reachable_masks)
            for used_mask in current_masks:
                if used_mask & word_mask.mask:
                    continue

                new_mask = used_mask | word_mask.mask
                if new_mask in parents:
                    continue

                parents[new_mask] = (used_mask, word_mask.word_index)
                reachable_masks.append(new_mask)
                if new_mask.bit_count() > best_mask.bit_count():
                    best_mask = new_mask

        best_result: List[int] = []
        while best_mask:
            previous_mask, word_index = parents[best_mask]
            best_result.append(word_index)
            best_mask = previous_mask

        best_result.reverse()
        return [valid_words[i] for i in best_result]

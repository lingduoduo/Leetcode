"""You'll implement this."""

from dataclasses import dataclass
from typing import Dict, List, Tuple

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

        Uses branch-and-bound with memoization to prune states that
        cannot beat the current best solution.
        """
        valid_words = self.word_list.valid_words()
        if not valid_words:
            return []

        # Convert alphabet to list for bit indexing
        alphabet = sorted(list(self.word_list.alphabet()))
        char_to_bit = {char: i for i, char in enumerate(alphabet)}

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

        # Explore higher-value words first so the bound becomes strong quickly.
        word_data.sort(key=lambda word: (word.char_count, word.mask.bit_count()), reverse=True)

        best_result: List[int] = []
        best_chars = 0

        # Try greedy first for a good baseline
        used_mask = 0
        greedy_result: List[int] = []
        for word_mask in word_data:
            if used_mask & word_mask.mask == 0:
                greedy_result.append(word_mask.word_index)
                used_mask |= word_mask.mask
                best_chars += word_mask.char_count

        best_result = greedy_result

        suffix_union = [0] * (len(word_data) + 1)
        for i in range(len(word_data) - 1, -1, -1):
            suffix_union[i] = suffix_union[i + 1] | word_data[i].mask

        seen: Dict[Tuple[int, int], int] = {}
        current_result: List[int] = []

        def search(start: int, current_mask: int, current_chars: int) -> None:
            nonlocal best_chars, best_result

            remaining_bound = (suffix_union[start] & ~current_mask).bit_count()
            if current_chars + remaining_bound <= best_chars:
                return

            state = (start, current_mask)
            if seen.get(state, -1) >= current_chars:
                return
            seen[state] = current_chars

            if current_chars > best_chars:
                best_chars = current_chars
                best_result = list(current_result)

            for i in range(start, len(word_data)):
                word_mask = word_data[i]
                if current_mask & word_mask.mask != 0:
                    continue

                current_result.append(word_mask.word_index)
                search(i + 1, current_mask | word_mask.mask, current_chars + word_mask.char_count)
                current_result.pop()

        search(0, 0, 0)

        return [valid_words[i] for i in best_result]

"""Find words that contain other words as substrings."""

from typing import List

from word_list import WordList


class Solver:
    def __init__(self, word_list: WordList) -> None:
        self.word_list = word_list

    def find_containers(self) -> List[str]:
        """
        Find all words that contain at least one other word as a substring.

        Returns:
            List of words that contain other words from the list.
            A word cannot contain itself.

        Example:
            ["apple", "app", "banana", "nana"] -> ["apple", "banana"]
            ["cat", "dog", "bird"] -> []
        """
        words = self.word_list.get_words()
        word_set = self.word_list.get_word_set()
        candidate_lengths = sorted({len(word) for word in word_set})
        containers: List[str] = []

        for word in words:
            word_length = len(word)

            for candidate_length in candidate_lengths:
                if candidate_length >= word_length:
                    break

                max_start = word_length - candidate_length + 1
                for start in range(max_start):
                    if word[start:start + candidate_length] in word_set:
                        containers.append(word)
                        break
                else:
                    continue

                break

        return containers

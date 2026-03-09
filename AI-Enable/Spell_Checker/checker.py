"""You'll implement this."""

from typing import Dict, List

from distance import EditDistance


class Checker:
    """Suggests spelling corrections ranked by edit distance and frequency."""

    def __init__(self, dictionary: Dict[str, int]):
        self.dictionary = dictionary
        self.ed = EditDistance()

    def suggest(self, word: str, max_distance: int = 2, max_suggestions: int = 5) -> List[str]:
        if max_suggestions <= 0:
            return []
        if word in self.dictionary:
            return [word]

        # Get all words within the max_distance, sorted by distance then frequency
        candidates = self.ed.closest_words(word, self.dictionary, max_distance)

        # Return just the words (first element of each tuple), limited by max_suggestions
        return [candidate[0] for candidate in candidates[:max_suggestions]]

from typing import List
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)

        if n < total_len:
            return []

        target = Counter(words)
        res = []

        for start in range(word_len):
            left = start
            seen = defaultdict(int)
            count = 0

            for right in range(start, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    seen[word] += 1
                    count += 1

                    while seen[word] > target[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        res.append(left)

                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return res
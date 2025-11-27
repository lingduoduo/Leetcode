from typing import List
import collections


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        freq = [0] * 26
        for c in words[0]:
            freq[ord(c) - ord('a')] += 1
        for i in range(1, len(words)):
            current_freq = [0] * 26
            for c in words[i]:
                current_freq[ord(c) - ord('a')] += 1
            for k in range(26):
                freq[k] = min(freq[k], current_freq[k])
        for i in range(26):
            while freq[i] != 0:
                result.extend(chr(i + ord('a')))
                freq[i] -= 1
        return result


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = collections.Counter(words[0])
        for word in words[1:]:
            freq &= collections.Counter(word)
        res = []
        for k, v in freq.items():
            res.extend([k] * v)
        return res
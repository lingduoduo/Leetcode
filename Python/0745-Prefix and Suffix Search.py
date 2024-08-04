from typing import List
import collections


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += "#"
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for letter in suff + "#" + pref:
            if letter not in cur:
                return -1
            cur = cur[letter]
        return cur[WEIGHT]


Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False


class WordFilter:
    def __init__(self, words):
        from collections import defaultdict

        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.weights = {}
        for index, word in enumerate(words):
            prefix, suffix = "", ""
            for char in [""] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in [""] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            self.weights[word] = index

    def f(self, prefix, suffix):
        weight = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight


class WordFilter:
    def __init__(self, words):
        self.inputs = {}
        for index, word in enumerate(words):
            prefix = ""
            for char in [""] + list(word):
                prefix += char
                suffix = ""
                for char in [""] + list(word[::-1]):
                    suffix += char
                    self.inputs[prefix + "." + suffix[::-1]] = index

    def f(self, prefix, suffix):
        return self.inputs.get(prefix + "." + suffix, -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

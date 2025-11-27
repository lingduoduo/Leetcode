import collections
from typing import List

class MagicDictionary:
    """
    Input: buildDict(["hello", "leetcode"]), Output: Null
    Input: search("hello"), Output: False
    Input: search("hhllo"), Output: True
    Input: search("hell"), Output: False
    Input: search("leetcoded"), Output: False
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []
        self.near = {}

    def _candidate(self, word):
        for i in range(len(word)):
            yield word[:i] + "*" + word[i + 1 :]

    def buildDict(self, words):
        self.words = set(words)
        self.near = collections.Counter(
            [_ for word in words for _ in self._candidate(word)]
        )
        print(self.near)

    def search(self, word) -> bool:
        return any(
            self.near[cand] > 1 or self.near[cand] == 1 and word not in self.words
            for cand in self._candidate(word)
        )


class MagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(
            sum(a != b for a, b in zip(word, candidate)) == 1
            for candidate in self.buckets[len(word)]
        )


class MagicDictionary:
    def __init__(self):
        pass

    def _genneighbors(self, word):
        for i in range(len(word)):
            yield word[:i] + "*" + word[i + 1 :]

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        self.d = collections.Counter(
            nei for word in dictionary for nei in self._genneighbors(word)
        )

    def search(self, searchWord: str) -> bool:
        return any(
            self.d[nei] > 1 or self.d[nei] == 1 and searchWord not in self.words
            for nei in self._genneighbors(searchWord)
        )


class MagicDictionary:

    def __init__(self):
        self.d = collections.defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            n = len(word)
            self.d[n].add(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        if n not in self.d: return False

        def diff(word1, word2):
            res = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    res += 1
                if res > 1:
                    return res
            return res

        for word in self.d[n]:
            if diff(word, searchWord) == 1:
                return True
        return False


import collections
from typing import List

class MagicDictionary:

    def __init__(self):
        self.root = {}   # trie root
    
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.root
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = True   # end marker

    # DFS search allowing exactly 1 difference
    def dfs(self, node, word, index, used_diff):
        # Reached end of searchWord
        if index == len(word):
            return used_diff == 1 and "#" in node

        c = word[index]

        for ch in node.keys():
            if ch == "#":
                continue

            # If characters match → continue without consuming diff
            if ch == c:
                if self.dfs(node[ch], word, index + 1, used_diff):
                    return True
            else:
                # If they differ → consume the one allowed diff
                if used_diff == 0:
                    if self.dfs(node[ch], word, index + 1, 1):
                        return True

        return False

    def search(self, searchWord: str) -> bool:
        return self.dfs(self.root, searchWord, 0, 0)


if __name__ == "__main__":
    obj = MagicDictionary()
    obj.buildDict(["hello", "leetcode"])
    result = obj.search("hello")
    print(result)

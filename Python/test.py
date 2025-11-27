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
    def dfs(self, node, word, index, diff):
        # Reached end of searchWord
        if index == len(word):
            return diff == 1 and "#" in node

        c = word[index]

        for ch in node.keys():
            if ch == "#":
                continue

            # If characters match → continue without consuming diff
            if ch == c:
                if self.dfs(node[ch], word, index + 1, diff):
                    return True
            else:
                # If they differ → consume the one allowed diff
                if diff == 0:
                    if self.dfs(node[ch], word, index + 1, 1):
                        return True

        return False

    def search(self, searchWord: str) -> bool:
        return self.dfs(self.root, searchWord, 0, 0)

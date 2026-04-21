from collections import defaultdict, deque
from typing import List
import math
import heapq
import bisect

class trie:
   def __init__(self):
       self.d = {}

   def addWord(self, word: str):
       d = self.d
       for ch in word:
           if ch not in d:
               d[ch] = {}
           d = d[ch]
        d['#'] = True

   def search(self, word: str):
       return self.dfs(word, d)
       d = self.d
       for ch in word:
           if "#" in d:
               return d["#"]
           if ch not in d:
               return word
           d = d[ch]
       return d['#'] if '#' in d else word


class MagicDictionary:

    def __init__(self):
        self.d = {}
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            d = self.d
            for ch in word:
                if ch not in d:
                    d[ch] = {}
                d = d[ch]
            d["#"] = True   
        
    def search(self, searchWord: str) -> bool:
        n = len(searchWord)

        def dfs(d, i, changed):
            if i == n:
                return changed and "#" in node

            ch = searchWord[i]
            for nxt_ch, nxt_d in d.items():
                if nxt_ch == "#":
                    continue

                if nxt_ch == ch:
                    if dfs(nxt_d, i + 1, changed):
                        return True
                else:
                    if not changed and dfs(nxt_d, i + 1, True):
                        return True

            return False

        return dfs(self.root, 0, False)


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = WordDictionary()
        for word in dictionary:
            trie.addWord(word)
        
        res = []
        for word in sentence.split():
            res.append(trie.search(word))
        return ' '.join(res)

if __name__ == "__main__":
    res = Solution().replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery")
    print(res)

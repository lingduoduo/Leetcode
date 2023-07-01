from functools import reduce
from typing import List
import collections


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word):
            for i in range(len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return "".join(map(replace, sentence.split()))


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in dictionary:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        osf = ''
        for c in word:
            if c not in node.children: break
            node = node.children[c]
            osf += c
            if node.isWord: return osf
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for words in dictionary:
            trie.insert(words)
        res = ''
        for word in sentence.split():
            if res:
                res += ' '
            res += trie.search(word)
        return res

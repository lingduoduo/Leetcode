from collections import defaultdict

class WordDictionary:
    def __init__(self):
        """Initialize your data structure here."""
        self.trie = {}

    def addWord(self, word: str) -> None:
        """Adds a word into the data structure."""
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["#"] = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter."""
        return self.dfs(self.trie, word, 0)

    def dfs(self, dic, word, i):
        if i == len(word):
            return "#" in dic

        if word[i] == ".":
            for child in dic:
                if child != "#" and self.dfs(dic[child], word, i + 1):
                    return True
            return False

        if word[i] not in dic:
            return False
        return self.dfs(dic[word[i]], word, i + 1)


class WordDictionary:

    def __init__(self):
        self.d = defaultdict(dict)
        

    def addWord(self, word: str) -> None:
        d = self.d
        for ch in word:
            if ch not in d:
                d[ch] = {}
            d = d[ch]
        d["#"] = True
    
    def search(self, word: str) -> bool:
        def dfs(d, i):
            if i == len(word):
                return "#" in d

            ch = word[i]
            if ch == ".":
                for c in d:
                    if c != "#" and dfs(d[c], i + 1):
                        return True
                return False
            else:
                if ch not in d:
                    return False
                return dfs(d[ch], i + 1)

        return dfs(self.d, 0)


if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    ###result = obj.search("pad")
    ###print(result)
    result = obj.search("bad")
    print(result)
    ###result = obj.search(".ad")
    ###print(result)
    ###result = obj.search("b..")
    ###print(result)

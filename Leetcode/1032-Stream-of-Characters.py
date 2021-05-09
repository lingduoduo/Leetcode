class Trie:
    def __init__(self):
        """ Initialize your data structure here. """
        self.dic = {}

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie. """
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True
        
    def search(self, word: list) -> bool:
        """ Returns if the word is in the trie. """
        cur = self.dic
        for c in word:
            if '#' in cur:
                return True
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])
        self.s = deque()
        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
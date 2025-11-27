class Trie:
    def __init__(self):
        """Initialize your data structure here."""
        self.d = {}

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        cur = self.d
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["#"] = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        cur = self.d
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return "#" in cur

    def startsWith(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        cur = self.d
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True


class TrieNode:
    def __init__(self):
        # Stores children nodes and whether node is the end of a word
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        # Insert character by character into trie
        for c in word:
            # if character path does not exist, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        # Search character by character in trie
        for c in word:
            # if character path does not exist, return False
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        # Same as search, except there is no isEnd condition at final return
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


if __name__ == "__main__":
    obj = Trie()
    obj.insert("apple")
    obj.search("apple")
    obj.insert("apps")
    obj.startsWith("app")
    obj.insert("app")
    obj.startsWith("app")
    # print(result)
    # obj.insert("app");
    # result = obj.search("app")
    # print(result)
###Your Trie object will be instantiated and called as such:

###obj.insert(word)
###param_2 = obj.search(word)
###param_3 = obj.startsWith(prefix)

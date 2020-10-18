'''
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
'''


class Node:
    
    def __init__(self):
        self.d = dict()
        self.isword = False


class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        
        for i in range(len(word)):
            node = Node()
            current.d[word[i]] = current.d.get(word[i], node)
            current = current.d[word[i]]
        current.isword = True
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        
        for i in range(len(word)):
            if word[i] in current.d:
                current = current.d[word[i]]
            else:
                return False
        
        return current.isword
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        
        for i in range(len(prefix)):
            if prefix[i] in current.d:
                current = current.d[prefix[i]]
            else:
                return False
        return True


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
        print(self.dic)

    def search(self, word: str) -> bool:
        """ Returns if the word is in the trie. """
        cur = self.dic
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        """ Returns if there is any word in the trie that starts with the given prefix. """
        cur = self.dic
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    obj.insert("apps")
    # result = obj.search("apple")
    # result = obj.startsWith("app")
    # print(result)
    # result = obj.startsWith("tpp")
    # print(result)
    # obj.insert("app");
    # result = obj.search("app")
    # print(result)

###Your Trie object will be instantiated and called as such:

###obj.insert(word)
###param_2 = obj.search(word)
###param_3 = obj.startsWith(prefix)

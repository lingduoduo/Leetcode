import collections
import pysnooper


'''addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''

class Node(object):
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.isword = False

class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
    
    @pysnooper.snoop()
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        
        for i in range(len(word)):
            current = current.child[word[i]]
        current.isword = True
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.match(word, 0, self.root)
    
    @pysnooper.snoop()
    def match(self, word, idx, root):
        if not root:
            return False
        if idx == len(word):
            return root.isword
        
        if word[idx] != '.':
            return not root and self.match(word, idx + 1, root.child.get(word[idx]))
        else:
            for i in root.child.values():
                if self.match(word, idx + 1, i):
                    return True
            return False

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    # result = obj.search("pad")
    # print(result)
    result = obj.search("bad")
    print(result)
    # result = obj.search(".ad")
    # print(result)
    # result = obj.search("b..")
    # print(result)
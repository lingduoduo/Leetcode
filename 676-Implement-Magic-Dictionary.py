class MagicDictionary:
    '''
    Input: buildDict(["hello", "leetcode"]), Output: Null
    Input: search("hello"), Output: False
    Input: search("hhllo"), Output: True
    Input: search("hell"), Output: False
    Input: search("leetcoded"), Output: False
    '''
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = list()
    
    def buildDict(self, dict) -> None:
        """
        Build a dictionary through a list of words
        """
        
        for i in range(len(dict)):
            if dict[i] not in self.d:
                self.d.append(dict[i])
    
    def search(self, word) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        
        for i in range(len(self.d)):
            if len(self.d[i]) != len(word):
                continue
            match = 0
            j = 0
            while j < len(word):
                if word[j] == self.d[i][j]:
                    match += 1
                j += 1
            if match == len(word) - 1:
                return True
        return False


if __name__ == '__main__':
    obj = MagicDictionary()
    obj.buildDict(["hello", "leetcode"])
    result = obj.search("hello")
    print(result)
    result = obj.search("heelo")
    print(result)
    result = obj.search("heel")
    print(result)

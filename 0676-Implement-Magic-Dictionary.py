import collections
class MagicDictionary:
    '''
    Input: buildDict(["hello", "leetcode"]), Output: Null
    Input: search("hello"), Output: False
    Input: search("hhllo"), Output: True
    Input: search("hell"), Output: False
    Input: search("leetcoded"), Output: False
    '''
    
    ###def __init__(self):
    ###    """
    ###    Initialize your data structure here.
    ###    """
    ###    self.d = list()
    
    ###def buildDict(self, dict) -> None:
    ###    """
    ###    Build a dictionary through a list of words
    ###    """
        
    ###    for i in range(len(dict)):
    ###        if dict[i] not in self.d:
    ###            self.d.append(dict[i])
    
    ###def search(self, word) -> bool:
    ###    """
    ###    Returns if there is any word in the trie that equals to the given word after modifying exactly one character
    ###    """
        
    ###    for i in range(len(self.d)):
    ###        if len(self.d[i]) != len(word):
    ###            continue
    ###        match = 0
    ###        j = 0
    ###        while j < len(word):
    ###            if word[j] == self.d[i][j]:
    ###                match += 1
    ###            j += 1
    ###        if match == len(word) - 1:
    ###            return True
    ###    return False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []
        self.near = {}

    def _candidate(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.near = collections.Counter([_ for word in words for _ in self._candidate(word)])
        print(self.near)

    def search(self, word) -> bool:
        return any(self.near[cand] > 1 or self.near[cand] == 1 and word not in self.words for cand in self._candidate(word))


if __name__ == '__main__':
    obj = MagicDictionary()
    obj.buildDict(["hello", "leetcode"])
    result = obj.search("hello")
    print(result)
    ###result = obj.search("heelo")
    ###print(result)
    ###result = obj.search("heel")
    ###print(result)

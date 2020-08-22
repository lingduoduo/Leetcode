class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList):
        
        def buildPath(pathdict, word, path):
            if word not in pathdict:
                res.append([word] + path)
                return
            for newword in pathdict[word]:
                buildPath(pathdict, newword, [word] + path)
        
        wordList = set(wordList)
        # wordList.remove(beginWord)
        # wordList.remove(endWord)
        
        d = list()
        visited = set()
        parents = dict()
        res = []
        
        d.append([beginWord, 1])
        visited.add(beginWord)
        
        while d:
            node, step = d.pop(0)
            if node == endWord:
                buildPath(parents, node, [])
            
            for i in range(len(node)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    w = node[:i] + j + node[i + 1:]
                    if w in wordList and w not in visited:
                        parents[w] = parents.get(w, []) + [node]
                        d.append([w, step + 1])
                        # wordList.remove(w)
                        visited.add(w)
        
        return res


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = Solution().findLadders(beginWord, endWord, wordList)
    print(result)
    
    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot"]
    # result = Solution().findLadders(beginWord, endWord, wordList)
    # print(result)
    
    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]
    # result = Solution().findLadders(beginWord, endWord, wordList)
    # print(result)
    
    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot", "dog", "cog", "pot", "dot"]
    # result = Solution().findLadders(beginWord, endWord, wordList)
    # print(result)
    
    # length = len(beginWord)
    # parents = {}
    # for word in wordlist:
    #     parents[word] = []
    # result = []
    # visited = set()
    # visited.add(beginWord)
    
    # while True:
    #     pre_level = visited
    #     visited = set()
    
    #     for word in pre_level:
    #         for i in range(length):
    #             left = word[:i]
    #             right = word[i+1:]
    #             for c in 'abcdefghijklmnopqrstuvwxyz':
    #                 if c != word[i]:
    #                     w = left + c + right
    #                     if w in wordlist:
    #                         parents[w].append(word)
    #                         visited.add(w)
    #     if len(visited) == 0:
    #         return []
    #     if endWord in visited:
    #         break
    # buildPath([],endWord)
    # return result

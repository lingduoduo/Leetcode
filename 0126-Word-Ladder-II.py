# class Solution:
#     def findLadders(self, beginWord: str, endWord: str,
#                     wordList):
        
#         def buildPath(pathdict, word, path):
#             if word not in pathdict:
#                 res.append([word] + path)
#                 return
#             for newword in pathdict[word]:
#                 buildPath(pathdict, newword, [word] + path)
        
#         wordList = set(wordList)
#         ###wordList.remove(beginWord)
#         ###wordList.remove(endWord)
        
#         d = list()
#         visited = set()
#         parents = dict()
#         res = []
        
#         d.append([beginWord, 1])
#         visited.add(beginWord)
        
#         while d:
#             node, step = d.pop(0)
#             if node == endWord:
#                 buildPath(parents, node, [])
            
#             for i in range(len(node)):
#                 for j in 'abcdefghijklmnopqrstuvwxyz':
#                     w = node[:i] + j + node[i + 1:]
#                     if w in wordList and w not in visited:
#                         parents[w] = parents.get(w, []) + [node]
#                         d.append([w, step + 1])
#                         ###wordList.remove(w)
#                         visited.add(w)
        
#         return res

# class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList):
    #     wordlist=set(wordList)
    #     res= []
    #     layer = {}
    #     layer[beginWord] = [[beginWord]]
        
    #     while layer:
    #         newlayer = collections.defaultdict(list)
    #         for w in layer:
    #             if w == endWord:
    #                 res.extend(k for k in layer[w])
    #             else:
    #                 for i in range(len(w)):
    #                     for c in "abcdefghijklmnopqrstuvwxyz":
    #                         newword=w[:i] + c + w[i+1:]
    #                         if newword in wordlist:
    #                             newlayer[newword] += [j+[newword] for j in layer[w]]
    #         wordlist -=set(newlayer.keys())
    #         layer = newlayer
            
    #     return res

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):

        wordList = set(wordList)
        stack = [(beginWord, [beginWord])]
        res = []

        while(stack):
            next_child = []
            for node, path in stack:
                if node == endWord:
                    res.append(path)

                for i in range(len(node)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        word = node[:i]+j+node[i+1:]
                        if word in wordList:
                            next_child.append((word, path+[word]))
            wordList -= set([n for n, p in next_child])
            stack = next_child

        return res


if __name__ == '__main__':
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # result = Solution().findLadders(beginWord, endWord, wordList)
    # print(result)

    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","dot","dog","lot","log"]
    # result = Solution().findLadders(beginWord, endWord, wordList)
    # print(result)

    beginWord = "red"
    endWord = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    result = Solution().findLadders(beginWord, endWord, wordList)
    print(result)

    ###beginWord = "hot"
    ###endWord = "dog"
    ###wordList = ["hot"]
    ###result = Solution().findLadders(beginWord, endWord, wordList)
    ###print(result)
    
    ###beginWord = "hot"
    ###endWord = "dog"
    ###wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]
    ###result = Solution().findLadders(beginWord, endWord, wordList)
    ###print(result)
    
    ###beginWord = "hot"
    ###endWord = "dog"
    ###wordList = ["hot", "dog", "cog", "pot", "dot"]
    ###result = Solution().findLadders(beginWord, endWord, wordList)
    ###print(result)
    
    ###length = len(beginWord)
    ###parents = {}
    ###for word in wordlist:
    ###    parents[word] = []
    ###result = []
    ###visited = set()
    ###visited.add(beginWord)
    
    ###while True:
    ###    pre_level = visited
    ###    visited = set()
    
    ###    for word in pre_level:
    ###        for i in range(length):
    ###            left = word[:i]
    ###            right = word[i+1:]
    ###            for c in 'abcdefghijklmnopqrstuvwxyz':
    ###                if c != word[i]:
    ###                    w = left + c + right
    ###                    if w in wordlist:
    ###                        parents[w].append(word)
    ###                        visited.add(w)
    ###    if len(visited) == 0:
    ###        return []
    ###    if endWord in visited:
    ###        break
    ###buildPath([],endWord)
    ###return result

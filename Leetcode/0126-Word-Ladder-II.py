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
        ###wordList.remove(beginWord)
        ###wordList.remove(endWord)

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
                        ###wordList.remove(w)
                        visited.add(w)

        return res


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordlist = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            newword = w[:i] + c + w[i + 1:]
                            if newword in wordlist:
                                newlayer[newword] += [j + [newword] for j in layer[w]]
            wordlist -= set(newlayer.keys())
            layer = newlayer

        return res


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)
        res = []
        edge = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                edge[word[:i] + "_" + word[i + 1:]].append(word)

        q = {beginWord: [[beginWord]]}
        while q:
            wordList -= set(q.keys())
            new_q = collections.defaultdict(list)
            for w in q:
                if w == endWord:
                    res += q[w]
                else:
                    for i in range(len(w)):
                        for neww in edge[w[:i] + "_" + w[i + 1:]]:
                            if neww in wordList:
                                new_q[neww] += [j + [neww] for j in q[w]]
            q = new_q
        return res


class Solution:
    WILDCARD = "."

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Given a wordlist, we perform BFS traversal to generate a word tree where
        every node points to its parent node.

        Then we perform a DFS traversal on this tree starting at the endWord.
        """
        if endWord not in wordList:
            # end word is unreachable
            return []

        # first generate a word tree from the wordlist
        word_tree = self.getWordTree(beginWord, endWord, wordList)

        # then generate a word ladder from the word tree
        return self.getLadders(beginWord, endWord, word_tree)

    def getWordTree(self,
                    beginWord: str,
                    endWord: str,
                    wordList: List[str]) -> Dict[str, List[str]]:
        """
        BFS traversal from begin word until end word is encountered.

        This functions constructs a tree in reverse, starting at the endWord.
        """
        # Build an adjacency list using patterns as keys
        # For example: ".it" -> ("hit"), "h.t" -> ("hit"), "hi." -> ("hit")
        adjacency_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + Solution.WILDCARD + word[i + 1:]
                adjacency_list[pattern].append(word)

        # Holds the tree of words in reverse order
        # The key is an encountered word.
        # The value is a list of preceding words.
        # For example, we got to beginWord from no other nodes.
        # {a: [b,c]} means we got to "a" from "b" and "c"
        visited_tree = {beginWord: []}

        # start off the traversal without finding the word
        found = False

        q = deque([beginWord])
        while q and not found:
            n = len(q)

            # keep track of words visited at this level of BFS
            visited_this_level = {}

            for i in range(n):
                word = q.popleft()

                for i in range(len(word)):
                    # for each pattern of the current word
                    pattern = word[:i] + Solution.WILDCARD + word[i + 1:]

                    for next_word in adjacency_list[pattern]:
                        if next_word == endWord:
                            # we don't return immediately because other
                            # sequences might reach the endWord in the same
                            # BFS level
                            found = True
                        if next_word not in visited_tree:
                            if next_word not in visited_this_level:
                                visited_this_level[next_word] = [word]
                                # queue up next word iff we haven't visited it yet
                                # or already are planning to visit it
                                q.append(next_word)
                            else:
                                visited_this_level[next_word].append(word)

            # add all seen words at this level to the global visited tree
            visited_tree.update(visited_this_level)

        return visited_tree

    def getLadders(self,
                   beginWord: str,
                   endWord: str,
                   wordTree: Dict[str, List[str]]) -> List[List[str]]:
        """
        DFS traversal from endWord to beginWord in a given tree.
        """

        def dfs(node: str) -> List[List[str]]:
            if node == beginWord:
                return [[beginWord]]
            if node not in wordTree:
                return []

            res = []
            parents = wordTree[node]
            for parent in parents:
                res += dfs(parent)
            for r in res:
                r.append(node)
            return res

        return dfs(endWord)


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = Solution().findLadders(beginWord, endWord, wordList)
    print(result)

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    result = Solution().findLadders(beginWord, endWord, wordList)
    print(result)

    beginWord = "red"
    endWord = "tax"
    wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    result = Solution().findLadders(beginWord, endWord, wordList)
    print(result)

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot"]
    result = Solution().findLadders(beginWord, endWord, wordList)
    print(result)

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]
    result = Solution().findLadders(beginWord, endWord, wordList)
    print(result)

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog", "cog", "pot", "dot"]
    result = Solution().findLadders(beginWord, endWord, wordList)
    print(result)

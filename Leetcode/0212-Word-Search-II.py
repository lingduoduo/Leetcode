class Trie:
    def __init__(self):
        self.root = {}
        self.result = []

    def insertWord(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["_end_"] = word

    def getNextNode(self, letter, node):
        return node.get(letter)

    def checkNodeIsWordEnd(self, node):
        if "_end_" in node:
            self.result.append(node["_end_"])
            del node["_end_"]


class Solution:
    def __init__(self):
        self.board = self.visited = None
        self.m = self.n = 0
        self.trie = Trie()
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def initialize(self, board, words):
        self.board = board
        self.m = len(board)
        self.n = len(board[0]) if self.m else 0
        self.visited = [[False for j in range(self.n)] for i in range(self.m)]

        for word in words:
            self.trie.insertWord(word)

    def performDFSFromEachElement(self):
        for i, rows in enumerate(self.board):
            for j, ele in enumerate(rows):
                self.DFS(i, j, ele, self.trie.root)

    def DFS(self, i, j, letter, node):
        node = self.trie.getNextNode(letter, node)

        if not node:
            return None

        self.trie.checkNodeIsWordEnd(node)

        self.visited[i][j] = True
        self.checkNeighbors(i, j, node)
        self.visited[i][j] = False

    def checkNeighbors(self, i, j, node):
        for deltaX, deltaY in self.directions:
            neighborI, neighborJ = i + deltaX, j + deltaY
            if (
                -1 < neighborI < self.m
                and -1 < neighborJ < self.n
                and not self.visited[neighborI][neighborJ]
            ):
                self.DFS(neighborI, neighborJ, self.board[neighborI][neighborJ], node)

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        # approach: use a trie to save all words and perform dfs on board

        self.initialize(board, words)
        self.performDFSFromEachElement()

        return self.trie.result

from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]
            cur["#"] = word

        m, n = len(board), len(board[0])
        self.res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    self.dfs(board, i, j, trie)
        return self.res

    def dfs(self, board, x, y, trie):
        letter = board[x][y]
        m, n = len(board), len(board[0])
        cur = trie[letter]
        word = cur.pop("#", False)
        if word:
            self.res.append(word)
        board[x][y] = "*"
        for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            curx, cury = x + dirx, y + diry
            if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                self.dfs(board, curx, cury, cur)
        board[x][y] = letter
        if not cur:
            trie.pop(letter)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, trie):
            letter = board[x][y]
            m, n = len(board), len(board[0])
            cur = trie[letter]
            word = cur.pop("#", False)
            if word:
                res.append(word)
            board[x][y] = "*"
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            board[x][y] = letter
            if not cur:
                trie.pop(letter)

        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]
            cur["#"] = word

        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res


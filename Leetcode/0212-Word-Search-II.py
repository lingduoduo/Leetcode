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
        node['_end_'] = word

    def getNextNode(self, letter, node):
        return node.get(letter)

    def checkNodeIsWordEnd(self, node):
        if '_end_' in node:
            self.result.append(node['_end_'])
            del node['_end_']

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
            if -1 < neighborI < self.m and -1 < neighborJ < self.n and not self.visited[neighborI][neighborJ]:
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
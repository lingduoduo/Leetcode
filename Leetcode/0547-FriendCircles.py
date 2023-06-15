class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ###Method 1
        ### 	if M is None:
        ### 		return 0;
        ### 	n = len(M)
        ### 	visited = dict()
        ### 	results = 0
        ### 	for i in range(n):
        ### 		for j in range(n):
        ### 			group = hm.setdefault(i, set())
        ### 			if M[i][j] ==1:
        ### 				group.add(j)

        ### 	allNodes = set()
        ### 	for i in range(n):
        ### 		allNodes.add(i)
        ### 	while len(allNode) != 0:
        ### 		result += 1
        ### 		root = None
        ### 		for node in allNodes:
        ### 			root = node
        ### 			break
        ### 		self.dfs(root, set(), allNodes, hm)
        ### 	return result

        ###def dfs(self, root, visited, allNodes, hm):
        ###	visited.add(root)
        ###	allNodes.discard(root)
        ###	unvisited = set()
        ###	for node in hm.get(root):
        ###		if node not in visited:
        ###			unvisited.add(node)
        ###	for node in unvisited:
        ###		self.dfs(node, visited, allNodes, hm)

        ###Method 2
        ###	def dfs(M, curr, n):
        ###		for i in range(n):
        ### 		if M[curr][i] == 1:
        ### 			M[curr][i] = M[i][curr] = 0
        ### 		dfs(M, i, n)

        ###n = len(M)
        ###results = 0
        ###for i in range(n):
        ###	if M[i][i] == 1:
        ###		results += 1
        ###		dfs(M, i, n)
        ###return


class Solution(object):
    def findCircleNum(self, M):
        cnt, n = 0, len(M)
        self.vset = set()
        for x in range(n):
            if x not in self.vset:
                cnt += 1
                self.dfs(M, x)
        return cnt

    def dfs(self, M, n):
        for x in range(len(M)):
            if M[n][x] and x not in self.vset:
                self.vset.add(x)
                self.dfs(M, x)

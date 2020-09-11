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
        
        ###Method 3
        self.res = 0
        self.visited = [0] * len(M[0])
        
        for i in range(len(M)):
            if self.visited[i] == 0 and M[i][i] == 1:
                self.res += 1
                self.dfs(M, i)
                self.visited[i] = 1
        return self.res
    
    def dfs(self, M, curr):
        for j in range(len(M[curr])):
            if M[curr][j] == 1:
                M[curr][j] = 0
                M[j][curr] = 0
                self.dfs(M, j)

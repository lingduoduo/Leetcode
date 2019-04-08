class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(graph, 0, [0])
        return self.res

    def dfs(self, graph, curr, path):
        if graph[curr] == []:
            self.res.append(path)
            return
        for node in graph[curr]:
            self.dfs(graph, node, path + [node])

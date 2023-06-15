class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        ###0 = unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses

        self.res = []

        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return []
        return self.res

    def dfs(self, graph, visited, node):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True

        visited[node] = 1
        for j in graph[node]:
            if not self.dfs(graph, visited, j):
                return False
        visited[node] = 2
        self.res.append(node)
        return True

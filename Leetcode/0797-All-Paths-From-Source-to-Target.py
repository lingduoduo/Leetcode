# class Solution(object):
#     def allPathsSourceTarget(self, graph):
#         """
#         :type graph: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         self.res = []
#         self.dfs(graph, 0, [0])
#         return self.res

#     def dfs(self, graph, curr, path):
#         if graph[curr] == []:
#             self.res.append(path)
#             return
#         for node in graph[curr]:
#             self.dfs(graph, node, path + [node])


class Solution(object):
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        res = []
        stack = [[0]]

        while stack:
            m = len(stack)
            for i in range(m):
                path = stack.pop(0)
                if path[-1] == n - 1:
                    res.append(path)
                    continue

                for node in graph[path[-1]]:
                    print(node)
                    stack.append(path + [node])
        return res


if __name__ == "__main__":
    graph = [[1, 2], [3], [3], []]
    res = Solution().allPathsSourceTarget(graph)
    print(res)

import collections
from typing import List


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ####sort children and post order traversal

        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)

        for frm, tos in graph.items():
            tos.sort(reverse=True)

        result = list()

        def dfs(graph, source):
            while graph[source]:
                v = graph[source].pop()
                dfs(graph, v)
            result.append(source)

        dfs(graph, "JFK")
        return result[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backtracking(path, cur):
            if len(path) == len(tickets) + 1:  # 终止条件：路径长度等于机票数量+1
                results.append(path)  # 将当前路径添加到结果列表
                return True

            for i, ticket in enumerate(tickets):  # 遍历机票列表
                if ticket[0] == cur and used[i] == 0:  # 找到起始机场为cur且未使用过的机票
                    used[i] = 1  # 标记该机票为已使用
                    state = backtracking(path + [ticket[1]], ticket[1])  # 递归搜索
                    used[i] = 0  # 标记该机票为未使用
                    if state:
                        return True  # 只要找到一个可行路径就返回，不继续搜索

        tickets.sort()  # 先排序，这样一旦找到第一个可行路径，一定是字母排序最小的
        used = [0] * len(tickets)
        path = ["JFK"]
        results = []
        backtracking(path, "JFK")
        return results[0]

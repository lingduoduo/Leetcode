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


class Solution(object):
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for frm, tos in graph.items():
            tos.sort(reverse=True)
        res = []
        self.dfs(graph, "JFK", res)
        return res[::-1]

    def dfs(self, graph, source, res):
        while graph[source]:
            v = graph[source].pop()
            self.dfs(graph, v, res)
        res.append(source)
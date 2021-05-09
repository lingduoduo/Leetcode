import collections
class Solution:
    def isBipartite(self, graph) -> bool:
        visited = [0] * len(graph)# 0-not visited; 1-blue; 2-red;
        for i in range(len(graph)):
            if graph[i] and visited[i] == 0:
                visited[i] = 1
                q = collections.deque()
                q.append(i)
                while q:
                    v = q.popleft()#every point
                    for e in graph[v]:#every edge
                        if visited[e] != 0:
                            if visited[e] == visited[v]:
                                return False
                        else:
                            visited[e] = 3 - visited[v]
                            q.append(e)
        return True

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        edge = collections.defaultdict(list)
        for i in range(len(graph)):
            edge[i].extend(graph[i])
            for v in graph[i]:
                edge[v].append(i)
                
        N = len(graph)
        color = [0] * N
        for i in range(N):
            if color[i] == 0:
                q = [i]
                color[i] = 1
                while q:
                    cur = q.pop()
                    cur_c = color[cur]
                    for node in edge[cur]:
                        if color[node] == 0:
                            color[node] = cur_c * -1
                            q.append(node)
                        elif color[node] == cur_c:
                            return False
        return True

if __name__ == '__main__':
    graph = [[1,3],[0,2],[1,3],[0,2]]
    results = Solution().isBipartite(graph)
    print(results)

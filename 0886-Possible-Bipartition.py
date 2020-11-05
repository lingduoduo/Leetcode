class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edge = [[] for _ in range(N + 1)]
        for u, v in dislikes:
            edge[u].append(v)
            edge[v].append(u)
        color = [0] * (N + 1)
        for i in range(1, N + 1):
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
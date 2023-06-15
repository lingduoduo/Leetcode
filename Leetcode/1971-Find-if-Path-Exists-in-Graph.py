from typing import List
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        d = collections.defaultdict(list)
        for x, y in edges:
            d[x].append(y)

        stack = d[start]
        visited = [0] * n
        visited[start] = 1
        while stack:
            node = stack.pop(0)
            if node == end:
                return True
            elif visited[node] == 1:
                continue
            stack.extend(d[node])
            visited[node] = 1
        return False


if __name__ == "__main__":
    # res = Solution().validPath(n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2)
    # print(res)

    res = Solution().validPath(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], start=0, end=5
    )
    print(res)


# 10
# [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
# 7
# 5

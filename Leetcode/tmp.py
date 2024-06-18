import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = collections.defaultdict(list)
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])

        stack = [source]
        seen = set([source])
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for new_node in d[node]:
                if new_node not in seen:
                    seen.add(new_node)
                    stack.append(new_node)
        return False


if __name__ == "__main__":
    res = Solution().validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5)
    print(res)


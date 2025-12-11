from typing import List
from collections import defaultdict
import heapq

class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:
        d = defaultdict(set)          # s -> { e1, e2, ... } (s is prereq of e)
        pre = [0] * numCourses        # indegree
        for s, e in prerequisites:
            if e not in d[s]:         # avoid double counting indegree
                d[s].add(e)
                pre[e] += 1

        # topo queue: all nodes with indegree 0
        nodes = [i for i, v in enumerate(pre) if v == 0]

        # p[x] = all prerequisites (direct/indirect) of course x
        p = defaultdict(set)

        while nodes:
            node = nodes.pop(0)
            # propagate prerequisite sets to its neighbors
            for nxt in d[node]:                  # <-- use neighbors directly
                # all prereqs of `node` are also prereqs of `nxt`
                p[nxt] |= p[node]
                # and `node` itself is a prereq of `nxt`
                p[nxt].add(node)

                pre[nxt] -= 1
                if pre[nxt] == 0:
                    nodes.append(nxt)
        return [u in p[v] for (u, v) in queries]


if __name__ == "__main__":
    res = Solution().checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]])
    print(res)

# class Solution:
#     def findJudge(self, N: int, trust) -> int:
#         degree = [0]*N
#         for i in range(len(trust)):
#             f, t = trust[i]
#             degree[f-1] -= 1
#             degree[t-1] += 1
#         j = 0
#         print(degree)
#         while j < N:
#             if degree[j] == N-1:
#                 return j+1
#             j += 1
#         return -1

from typing import List
import collections


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        for x, y in trust:
            indegree[x].add(y)
            outdegree[y].add(x)
        for i in range(1, n + 1):
            if len(outdegree[i]) == n - 1 and i not in indegree:
                return i
        return -1


if __name__ == "__main__":
    N = 3
    trust = [[1, 3], [2, 3]]
    result = Solution().findJudge(N, trust)
    print(result)

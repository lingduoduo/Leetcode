import collections
import heapq
class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        d = collections.defaultdict(list)
        for i in range(len(edges)):
            fromNode, toNode = edges[i]
            d[fromNode].append((toNode, hasApple[toNode]))
            d[toNode].append((fromNode, hasApple[fromNode]))

        stack = [(0, 0)]
        visited = [0] * n

        res = set()
        tot = hasApple.count(True)

        # while any(hasApple):
        while stack:
            print(stack)
            dist, fromNode = heapq.heappop(stack)
            visited[fromNode] = 1
            for node, flag in d[fromNode]:
                if visited[node] == 0:
                    visited[node] = 1
                    dist += 1
                    heapq.heappush(stack, (dist, node))

                    if flag:
                        res.add((fromNode, node))
        return res
                    # if res == tot:
                    #   return 
                
# Output: 8 
# Explanation: The figure above represents the given tree where red vertices have an apple. 
# One optimal path to collect all apples is shown by the green arrows.  


if __name__ == '__main__':
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [False,False,True,False,True,True,False]
    results = Solution().minTime(n, edges, hasApple)
    print(results)

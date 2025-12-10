from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, c in enumerate(wells):
            graph[0].append((c, i + 1))

        for s, e, c in pipes:
            graph[s].append((c, e))
            graph[e].append((c, s))

        mst_set = set([0])
        heapq.heapify(graph[0])
        edges_heap = graph[0]
        res = 0
        while len(mst_set) < n + 1:
            c, nex = heapq.heappop(edges_heap)
            if nex not in mst_set:
                mst_set.add(nex)
                res += c
                for new_c, neighbor in graph[nex]:
                    if neighbor not in mst_set:
                        heapq.heappush(edges_heap, (new_c, neighbor))
        return res



class UnionFind:
    def __init__(self, size) -> None:
        self.group = list(range(size))
        self.rank = [0] * (size + 1)

    def find(self, person: int) -> int:
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, person_1: int, person_2: int) -> bool:
        group_1 = self.find(person_1)
        group_2 = self.find(person_2)
        if group_1 == group_2:
            return False

        # attach the group of lower rank to the group with higher rank
        if self.rank[group_1] > self.rank[group_2]:
            self.group[group_2] = group_1
        elif self.rank[group_1] < self.rank[group_2]:
            self.group[group_1] = group_2
        else:
            self.group[group_1] = group_2
            self.rank[group_2] += 1
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges = []
        for index, weight in enumerate(wells):
            ordered_edges.append((weight, 0, index+1))

        for house_1, house_2, weight in pipes:
            ordered_edges.append((weight, house_1, house_2))

        ordered_edges.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        total_cost = 0
        for cost, house_1, house_2 in ordered_edges:
            if uf.union(house_1, house_2):
                total_cost += cost
        return total_cost

if __name__ == "__main__":
    res = Solution().minCostToSupplyWater(n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]])
    print(res)

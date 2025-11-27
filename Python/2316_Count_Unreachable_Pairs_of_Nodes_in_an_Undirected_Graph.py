from collections import Counter
from itertools import accumulate
from typing import List
from operator import mul, add

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for u, v in edges: 
            dsu.union(u, v)
        print(dsu.group)
        counts = Counter(map(dsu.find, range(n))).values()
        return sum(map(mul, accumulate(counts, add, initial=0), counts))

class UnionFind:
   def __init__(self, size):
       self.group = [group_id for group_id in range(size)]
       self.rank = [0] * size


   def find(self, x):
       if self.group[x] != x:
           self.group[x] = self.find(self.group[x])
       return self.group[x]
  
   def union(self, a, b):
       group_a = self.find(a)
       group_b = self.find(b)
       if group_a == group_b:
           return False


       is_merged = True
       # Merge the lower-rank group into the higher-rank group.
       if self.rank[group_a] > self.rank[group_b]:
           self.group[group_b] = group_a
       elif self.rank[group_a] < self.rank[group_b]:
           self.group[group_a] = group_b
       else:
           self.group[group_a] = group_b
           self.rank[group_b] += 1

       return is_merged

if __name__ == "__main__":
    res = Solution().countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]])
    print(res)

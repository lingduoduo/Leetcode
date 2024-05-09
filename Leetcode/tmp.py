from typing import List, Optional
import heapq
from collections import defaultdict

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs_a = heapq.heapify([(cost[0], i) for i, cost in enumerate(costs)])
        costs_b = heapq.heapify([(cost[1], i) for i, cost in enumerate(costs)])
        cnt_a

    
# Test the code        
if __name__ == '__main__':
    res = Solution().twoCitySchedCost(costs = [[10,20],[30,200],[400,50],[30,20]])
    print(res)

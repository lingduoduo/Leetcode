class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        stack = collections.defaultdict(list)
        for num in nums:
            idx = stack[num-1]
            if not idx:
                n = 0
            else:
                n = heapq.heappop(idx)
            heapq.heappush(stack[num], n+1)
        for vals in stack.values():
            for val in vals:
                if val < 3:
                    return False
        return  True  
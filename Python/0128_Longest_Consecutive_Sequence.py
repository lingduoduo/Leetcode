class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in hash_set:
                cnt = 0
                while num + cnt in hash_set:
                    cnt += 1
                res = max(res, cnt)
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        nums = list(set(nums))
        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue
            current_length = 1
            cur = nums[i]
            while cur + 1 in nums_set:
                current_length += 1
                cur += 1
            res = max(res, current_length)
        return res

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        self.par[rx] = ry
        # union by size
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        self.size[rx] += self.size[ry]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        uf = UnionFind(len(nums))
        index = {v: i for i, v in enumerate(nums)}
        for v in nums:
            if v + 1 in index:
                uf.union(index[v], index[v + 1])
        return max(uf.size)
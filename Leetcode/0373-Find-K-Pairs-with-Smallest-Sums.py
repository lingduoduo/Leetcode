class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(nums, (num1+num2, num1, num2))
        res = []
        for x, num1, num2 in heapq.nsmallest(k, nums):
            res.append([num1, num2])
        return res
            
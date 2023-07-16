from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        nums = []
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(nums, (num1 + num2, num1, num2))
        res = []
        for x, num1, num2 in heapq.nsmallest(k, nums):
            res.append([num1, num2])
        return res


import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        res = []
        visited = set((0, 0))
        q = []
        heapq.heappush(q, (nums1[0] + nums2[0], 0, 0))
        for i in range(len(nums1) * len(nums2)):
            val, idx1, idx2 = heapq.heappop(q)
            res.append([nums1[idx1], nums2[idx2]])
            if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in visited:
                heapq.heappush(q, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
                visited.add((idx1 + 1, idx2))
            if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in visited:
                heapq.heappush(q, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
                visited.add((idx1, idx2 + 1))
            if len(res) == k:
                return res
        return res


if __name__ == "__main__":
    res = Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)
    print(res)

    res = Solution().kSmallestPairs(nums1=[1,1,2], nums2=[1,2,3], k=2)
    print(res)

    res = Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=10)
    print(res)

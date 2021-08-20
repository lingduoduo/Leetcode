# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         res = 0
#         l_max = 0
#         for i in range(len(arr)):
#             l_max = max(l_max, arr[i])
#             if l_max == i:
#                 res += 1
#         return res

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr:
            return 0

        res = 0
        right = arr[0]
        for i in range(len(arr)):
            right = max(right, arr[i])
            if right == i:
                res += 1
        return res
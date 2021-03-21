class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        l_max = 0
        for i in range(len(arr)):
            l_max = max(l_max, arr[i])
            if l_max == i:
                res += 1
        return res
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = collections.Counter(nums)
        res = 0
        for key, val in d.items():
            if k - key == key:
                res += val // 2
            elif key < k - key:
                res += min(val, d[k - key])
        return res

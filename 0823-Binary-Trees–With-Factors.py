class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = set(arr)

        @lru_cache(None)
        def dp(i):
            res = 1
            for num in arr:
                if i % num == 0 and i//num in arr:
                    res += dp(num) * dp(i//num) 
            return res

        return sum(dp(i) for i in arr) % (10 ** 9 + 7)

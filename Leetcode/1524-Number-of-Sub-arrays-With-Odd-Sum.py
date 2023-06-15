class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans, odd, even = 0, 0, 0
        for x in arr:
            if x % 2 == 1:
                odd, even = even + 1, odd
            else:
                odd, even = odd, even + 1
            ans += odd
        return ans % int(1e9 + 7)

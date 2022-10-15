from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        total = sum(ribbons)
        if k > total:
            return 0

        low, high = 1, min(total // k, max(ribbons))

        while low < high:
            mid = (low + high + 1) // 2
            if sum(x // mid for x in ribbons) >= k:
                low = mid
            else:
                high = mid - 1

        return low

if __name__ == "__main__":
    res = Solution().maxLength(ribbons = [9,7,5], k = 3)
    print(res)
from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canDistribute(mid: int) -> bool:
            count = 0
            for candy in candies:
                count += candy // mid
            return count >= k

        left, right = 1, max(candies) + 1
        result = 0

        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                result = mid
                left = mid + 1
            else:
                right = mid

        return result

if __name__ == "__main__":    # Example test cases
    solution = Solution()
    print(solution.maximumCandies([5, 8, 6], 3))  # Output: 5
    print(solution.maximumCandies([2, 5], 11))    # Output: 0
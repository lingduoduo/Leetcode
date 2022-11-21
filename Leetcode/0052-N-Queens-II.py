class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 9: return 352

        def canBe(nums):
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if i - j == nums[i] - nums[j] or j - i == nums[i] - nums[j]:
                        return False
            return True

        columnIndex = range(0, n)
        permutation = list(permutations(columnIndex, n))
        return sum(map(canBe, permutation))
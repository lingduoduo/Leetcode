from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA = sum(A)
        sumB = sum(B)
        setB = set(B)

        target = (sumA + sumB) // 2
        res = []

        for a in A:
            if target - (sumA - a) in setB:
                res.extend([a, target - (sumA - a)])
                return res


if __name__ == "__main__":
    A = [1, 1]
    B = [2, 2]
    res = Solution().fairCandySwap(A, B)
    print(res)

    A = [1, 2]
    B = [2, 3]
    res = Solution().fairCandySwap(A, B)
    print(res)

    A = [2]
    B = [1, 3]
    res = Solution().fairCandySwap(A, B)
    print(res)

# class Solution:
#     def maxRotateFunction(self, A) -> int:
#         if not A:
#             return 0
#         res = []
#         res.append(sum([idx * num for idx, num in enumerate(A)]))
#         for i in range(1, len(A)):
#             res.append(res[-1] + sum(A) - 4 * A[-i])
#         return max(res)


class Solution:
    def maxRotateFunction(self, A) -> int:
        if not A:
            return 0
        res = sum([idx * num for idx, num in enumerate(A)])
        curr = res
        for i in range(1, len(A)):
            curr = curr + sum(A) - len(A) * A[-i]
            res = max(res, curr)
        return res


if __name__ == "__main__":
    A = [4, 3, 2, 6]
    res = Solution().maxRotateFunction(A)
    print(res)

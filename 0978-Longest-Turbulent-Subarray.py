class Solution:
    def maxTurbulenceSize(self, A) -> int:
        maxAB, currA, currB = 1, 1, 1  # 初始化

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:  # 以第 i 个元素结尾，呈现升序的情况
                currA = currB + 1
                currB = 1
            elif A[i] < A[i - 1]:  # 以第 i 个元素结尾，呈现降序的情况
                currB = currA + 1
                currA = 1
            else:
                currA, currB = 1, 1  # 出现相等的情况，重新计数

            maxAB = max(maxAB, currA, currB)  # 更新最优值

        return maxAB


if __name__ == '__main__':
    # A = [9,4,2,10,7,8,8,1,9]
    # A = [0,1,1,0,1,0,1,1,0,0]
    A = [1,0,1,0]
    results = Solution().maxTurbulenceSize(A)
    print(results)

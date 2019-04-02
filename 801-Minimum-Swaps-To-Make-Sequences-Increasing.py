class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        keep = [float('inf')] * len(A)
        swap = [float('inf')] * len(A)

        keep[0] = 0
        swap[0] = 1

        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
        return min(keep[len(A) - 1], swap[len(A) - 1])


if __name__ == '__main__':
    A = [1, 3, 5, 4]
    B = [1, 2, 3, 7]
    result = Solution().minSwap(A, B)
    print(result)

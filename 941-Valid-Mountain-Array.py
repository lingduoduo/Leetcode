class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False
        if len(A) <= 2:
            return False

        curr = 1
        pos = 0
        neg = 0

        while curr < len(A):
            if A[curr - 1] < A[curr]:
                pos += 1
                curr += 1
            else:
                break
        while curr < len(A):
            if A[curr - 1] > A[curr]:
                neg += 1
                curr += 1
            else:
                break

        return pos > 0 and neg > 0 and 1 + pos + neg == len(A)
        # return([pos, neg])


if __name__ == "__main__":
    numbers = [0, 3, 2, 1]
    numbers = [2, 1]
    results = Solution().validMountainArray(numbers)
    print(results)

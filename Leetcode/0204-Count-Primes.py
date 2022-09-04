class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 0

        nums = [None] * n
        nums[0] = False
        nums[1] = False

        for i in range(2, n):
            if nums[i] == None:
                nums[i] = True
            for j in range(i + i, n, i):
                nums[j] = False

        return sum(nums)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2,n):
            if prime[i]:
                for j in range(i + i, n, i):
                    prime[j]=False
        return prime.count(True)

if __name__ == "__main__":
    res = Solution().countPrimes(n=10)
    print(res)
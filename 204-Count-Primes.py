class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n < 3: return 0
        # f = [1] * n
        # f[0] = f[1] = 0
        #
        # for i in range(2, int(n ** (1 / 2))):
        #     if not f[i]:
        #         continue
        #     j = 2
        #     while j * i < n:
        #         f[j * i] = 0
        #         j += 1
        # return sum(f)

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
        

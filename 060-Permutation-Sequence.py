class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = i*factorial[i-1]

        res = []
        nums = list(range(1,n+1))

        k-=1
        for i in range(n-1, -1, -1):
            a=k//factorial[i]
            res.append(str(nums[a]))
            nums.pop(a)
            k=k%factorial[i]

        return ''.join(res)

if __name__=="__main__":
    n=4
    k=9
    result = Solution().getPermutation(n, k)
    print(result)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = [i + 1 for i in range(n)]
        for i in range(k - 1):
            res = self.nextPermutation(res)
        return "".join([str(num) for num in res])

    def nextPermutation(self, nums):
        flag = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                flag = i
                break

        if flag == -1:
            nums.sort()
        else:
            for i in range(len(nums) - 1, flag, -1):
                if nums[i] > nums[flag]:
                    nums[i], nums[flag] = nums[flag], nums[i]
                    nums[flag + 1 :] = sorted(nums[flag + 1 :])
                    break
        return nums


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = [1] * n
        nums = [1]
        for i in range(1, n):
            factorial[i] = i * factorial[i - 1]
            nums.append(1 + i)

        res = []

        k -= 1
        for i in range(n - 1, -1, -1):
            a = k // factorial[i]
            res.append(str(nums[a]))
            nums.pop(a)
            k = k % factorial[i]

        return "".join(res)


if __name__ == "__main__":
    n = 4
    k = 9
    result = Solution().getPermutation(n, k)
    print(result)

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N

        nums = list(map(int, list(str(N))))

        idx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1] or (idx != len(nums) - 1 and nums[i] == nums[idx]):
                idx = i

        if idx == len(nums) - 1:
            return N

        res = nums[:idx]
        res.append(nums[idx] - 1)
        for i in range(idx + 1, len(nums)):
            res.append(9)

        return str(int("".join(map(str, res))))


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strs = list(str(n))

        for i in range(len(strs) - 1, 0, -1):
            if strs[i - 1] > strs[i]:
                strs[i - 1] = str(int(strs[i - 1]) - 1)
                for j in range(i, len(strs)):
                    strs[j] = "9"
        return int("".join(strs))


if __name__ == "__main__":
    res = Solution().monotoneIncreasingDigits(668841)
    print(res)

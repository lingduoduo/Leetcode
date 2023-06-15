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


if __name__ == "__main__":
    res = Solution().monotoneIncreasingDigits(668841)
    print(res)

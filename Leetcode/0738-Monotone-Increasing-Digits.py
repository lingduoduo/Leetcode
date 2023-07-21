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
    def monotoneIncreasingDigits(self, N: int) -> int:
        # 将整数转换为字符串
        strNum = list(str(N))

        # 从右往左遍历字符串
        for i in range(len(strNum) - 1, 0, -1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if strNum[i - 1] > strNum[i]:
                strNum[i - 1] = str(int(strNum[i - 1]) - 1)  # 将前一个字符减1
                # 将修改位置后面的字符都设置为9，因为修改前一个字符可能破坏了递增性质
                for j in range(i, len(strNum)):
                    strNum[j] = "9"

        # 将列表转换为字符串，并将字符串转换为整数并返回
        return int("".join(strNum))


if __name__ == "__main__":
    res = Solution().monotoneIncreasingDigits(668841)
    print(res)

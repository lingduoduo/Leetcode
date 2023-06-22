class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num


class Solution:
    def largestNumber(self, nums):
        cur = ""
        res = ""
        nums = [str(num) for num in nums]
        while nums:
            for i in nums:
                if not cur:
                    cur = i
                else:
                    if int(i + cur) > int(cur + i):
                        cur = i
            res += cur
            nums.remove(cur)
            cur = ""
        return str(int(res))


if __name__ == "__main__":
    result = Solution().largestNumber(nums=[3, 30, 34, 5, 9])
    print(result)

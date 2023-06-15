class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest_num[0] == "0" else largest_num


class Solution:
    def largestNumber(self, nums):
        current_max, ans = "", ""
        # Convert Ints into Strings

        nums = [str(i) for i in nums]
        while nums:
            for i in nums:
                if not current_max:
                    current_max = i
                else:
                    # Comparator
                    if i + current_max > current_max + i:
                        current_max = i
            ans += current_max
            nums.remove(current_max)
            current_max = ""
        return ans if not ans.startswith("0") else "0"


if __name__ == "__main__":
    result = Solution().largestNumber(nums=[3, 30, 34, 5, 9])
    print(result)

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        prev = lower - 1
        for i in range(1 + len(nums)):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                left = prev + 1
                right = curr - 1
                if left != right:
                    res.append(f"{left}->{right}")
                else:
                    res.append(f"{left}")
            prev = curr
        return res


if __name__ == "__main__":
    res = Solution().findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99)
    print(res)

    res = Solution().findMissingRanges(nums=[-1], lower=-1, upper=-1)
    print(res)

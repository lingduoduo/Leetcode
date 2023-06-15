import collections
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False


if __name__ == "__main__":
    input = [1, 2, 2]
    result = Solution().containsDuplicate(input)
    print(result)

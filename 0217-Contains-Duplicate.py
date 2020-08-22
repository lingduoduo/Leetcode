import collections


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # d = collections.Counter(nums)
        # for key, val in d.items():
        #     if val > 1:
        #         return True
        # return False
        
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    input = [1, 2]
    result = Solution().containsDuplicate(input)
    print(result)

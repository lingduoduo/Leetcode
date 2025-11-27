class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        nums = [1,2,3,1], k = 3
        """
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = i
            else:
                if i - d[num] <= k:
                    return True
                d[num] = i
        return False


if __name__ == "__main__":
    ###nums = [1, 2, 3, 1]
    ###k=3
    ###result = Solution().containsNearbyDuplicate(nums,k)
    ###print(result)

    ###nums = [1, 0, 1, 1]
    ###k = 1
    ###result = Solution().containsNearbyDuplicate(nums, k)
    ###print(result)

    nums = [99, 99]
    k = 2
    result = Solution().containsNearbyDuplicate(nums, k)
    print(result)

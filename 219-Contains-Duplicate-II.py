class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        nums = [1,2,3,1], k = 3
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], []) + [i]
            if len(d[nums[i]])>=2:
                if d[nums[i]][-1] - d[nums[i]][-2] <= k:
                    return True
        return False

if __name__ == '__main__':
    # nums = [1, 2, 3, 1]
    # k=3
    # result = Solution().containsNearbyDuplicate(nums,k)
    # print(result)

    nums = [1,0,1,1]
    k = 1
    result = Solution().containsNearbyDuplicate(nums,k)
    print(result)
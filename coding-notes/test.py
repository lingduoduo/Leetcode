class Solution:
    def binarySearch(self, nums, k):
        l = 0
        r = len(nums)
        
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= k:
                r = m 
            else:
                l = m + 1
        return l

    def getNumberofK(self, nums, k):
        first = self.binarySearch(nums, k)
        print(first)
        last = self.binarySearch(nums, k + 1)
        print(last)
        return 0 if first == len(nums) - 1 or nums[first] != k else last - first
    
if __name__ == '__main__':
    # nums = [1, 2, 3, 3, 3, 3, 4, 5]
    # res = Solution().getNumberofK(nums, 3)
    # print(res)

    nums = [2,2]
    res = Solution().getNumberofK(nums, 2)
    print(res)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums1, nums2 = 0, 0
        c1, c2 = 0, 0
        result = []
        for i in nums:
            if i == nums1:
                c1 += 1
            elif i == nums2:
                c2 += 1
            elif c1 == 0:
                nums1 = i
                c1 = 1
            elif c2 == 0:
                nums2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1 = 0
        c2 = 0
        for j in nums:
            if j == nums1:
                c1 += 1
            elif j == nums2:
                c2 += 1
                
        l = len(nums)
        if c1>l/3:
            result.append(nums1)
        if c2>l/3:
            result.append(nums2)
        return result
        
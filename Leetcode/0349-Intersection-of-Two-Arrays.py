class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ###result = set()
        #
        ###l1 = len(nums1)
        ###l2 = len(nums2)
        #
        ###if l1 < l2:
        ###    for i in range(l1):
        ###        if nums1[i] in nums2:
        ###            result.add(nums1[i])
        ###else:
        ###    for i in range(l2):
        ###        if nums2[i] in nums1:
        ###            result.add(nums2[i])
        ###return list(result)
        #
        ###return list(set(nums1) & set(nums2))

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        ref = set(nums2)
        res = set()
        for i in range(len(nums1)):
            if nums1[i] in ref:
                res.add(nums1[i])
        return res

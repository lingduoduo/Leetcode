class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
     
        curr1, curr2 = m - 1, n - 1
        k = m + n - 1
        while curr1 >= 0 and curr2 >= 0:
            if nums1[curr1] > nums2[curr2]:
                nums1[k] = nums1[curr1]
                curr1 -= 1
            else:
                nums1[k] = nums2[curr2]
                curr2 -= 1
            k -= 1
        while curr2 >= 0:
            nums1[k] = nums2[curr2]
            curr2 -= 1
            k -= 1


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        curr1 = m-1
        curr2 = n-1
        
        for i in range(m+n-1,0,-1):
        	if curr1<0:
        		nums1[:curr2]=nums[curr1]
        	elif curr2<0:
        		break
        	elif nums1[curr1] > nums2[curr2] and curr1>=0 and curr2>=0:
        		nums1[i] = nums1[curr1]
        		curr1-=1
        	elif nums1[curr1] <= nums2[curr2] and curr1>=0 and curr2>=0:
        		nums1[i] = nums2[curr2]
        		curr2-=1
     


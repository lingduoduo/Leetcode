class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        idx={}
        for i in range(len(nums2)):
            j = i+1
            while j<len(nums2) and nums2[i] >= nums2[j]:
                j += 1
            if j==len(nums2):
                idx[nums2[i]]=-1
            else:
                idx[nums2[i]]=nums2[j]

        print(idx)

        res = []
        for num in nums1:
            res.append(idx[num])
        return res

if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    result = Solution().nextGreaterElement(nums1, nums2)
    print(result)

            
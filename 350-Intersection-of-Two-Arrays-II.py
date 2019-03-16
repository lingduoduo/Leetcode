class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ## first try
        # result = list()
        # l1 = len(nums1)
        # l2 = len(nums2)
        # # if l1<l2:
        # #     for i in range(l1):
        # #         if nums1[i] in nums2:
        # #             result.append(nums1[i])
        # #             nums2.pop(nums2.index(nums1[i]))
        # # else:
        # #     for i in range(l2):
        # #         if nums2[i] in nums1:
        # #             result.append(nums2[i])
        # #             nums1.pop(nums1.index(nums2[i]))
        # # return list(result)
        # if l1>l2:
        #     nums1, nums2 = nums2, nums1


        ## second try
        cnt = dict()
        res = list()
        for i in range(len(nums1)):
            if nums1[i] in cnt:
                cnt[nums1[i]]+=1
            else:
                cnt[nums1[i]]=1

        for i in range(len(nums2)):
            if nums2[i] in cnt and cnt[nums2[i]]>0:
                res.append(nums2[i])
                cnt[nums2[i]]-=1
        return(res)

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    nums1=[4,9,5]
    nums2 = [9,4,9,8,4]
    result = Solution().intersection(nums1, nums2)
    print(result)


# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         idx={}
#         for i in range(len(nums2)):
#             j = i+1
#             while j<len(nums2) and nums2[i] >= nums2[j]:
#                 j += 1
#             if j==len(nums2):
#                 idx[nums2[i]]=-1
#             else:
#                 idx[nums2[i]]=nums2[j]

#         print(idx)

#         res = []
#         for num in nums1:
#             res.append(idx[num])
#         return res
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = []
        for i in reversed(range(len(nums2))):
            if not stack:
                d[nums2[i]] = -1
            else:
                if stack[-1] > nums2[i]:
                    d[nums2[i]] = stack[-1]
                else:
                    while stack and stack[-1] <= nums2[i]:
                        stack.pop()
                    if stack:
                        d[nums2[i]] = stack[-1]
                    else:
                        d[nums2[i]] = -1
            stack.append(nums2[i])
        res = [d[nums1[i]] for i in range(len(nums1))]
        return res



if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    # nums1 = [3,1,5,7,9,2,6]
    # nums2 = [1,2,3,5,6,7,9,11]
    result = Solution().nextGreaterElement(nums1, nums2)
    print(result)


            
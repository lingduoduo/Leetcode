# class Solution:
#     def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
#         res = 0
#         dic_num1 = {}
#         dic_num2 = {}

#         for i in range(len(nums1)):
#             for j in range(i+1,len(nums1)):
#                 v = nums1[i] * nums1[j]
#                 dic_num1[v] = dic_num1.setdefault(v,0) + 1

#         for i in range(len(nums2)):
#             for j in range(i+1,len(nums2)):
#                 v = nums2[i] * nums2[j]
#                 dic_num2[v] = dic_num2.setdefault(v,0) + 1

#         for i in nums1:
#             res += dic_num2.get(i * i,0)
#         for i in nums2:
#             res += dic_num1.get(i * i, 0)

#         return res

class Solution:
    def numTriplets(self, nums1, nums2) -> int:
        self.res = 0
        
        nums1.sort()
        nums2.sort()
        self.counting(nums1, nums2)
        self.counting(nums2, nums1)
        
        return self.res

    def counting(self, nums1, nums2):
        for i in range(len(nums1)):
            left = 0
            right = len(nums2)-1
            while left < right:
                if nums1[i]**2 == nums2[left] * nums2[right]:
                    if nums2[left] == nums2[right]:
                        self.res += (right-left+1)*(right-left)//2
                        break
                    else:
                        left2 = left
                        while left2 < right and nums2[left2] == nums2[left]:
                            left2 += 1
                        right2 = right
                        while left < right2 and nums2[right2] == nums2[right]:
                            right2 -= 1 
                        self.res += (left2-left)*(right-right2)
                        left = left2
                        right = right2  
                elif nums2[left] * nums2[right] < nums1[i]**2:
                    left += 1
                else:
                    right -= 1

# Output: 9
# Explanation: All Triplets are valid, because 1^2 = 1 * 1.
# Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
# Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].

# Type 1: , , (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
# Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].

if __name__ == '__main__':
    # nums1 = [7,4]
    # nums2 = [5,2,8,9]
    # nums1 = [1,1]
    # # nums2 = [1,1,1]
    # nums1 = [7,7,8,3]
    # nums2 = [1,2,9,7]

    # nums1 = [4,7,9,11,23]
    # nums2 = [3,5,1024,12,18]

    nums1= [4,1,4,1,12]
    nums2=[3,2,5,4]
    res = Solution().numTriplets(nums1, nums2)
    print(res)
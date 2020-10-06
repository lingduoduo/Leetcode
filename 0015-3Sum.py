# class Solution(object):
#     def threeSum(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: List[List[int]]
        # """
        ###nums = sorted(nums)
        ###if not nums or nums[0]>0 or nums[len(nums)-1]<0: return []
        ###res = []
        ###for i in range(len(nums)-2):
        ###    if i>0 and nums[i] == nums[i-1]:
        ###        continue
        ###    target = -nums[i]
        ###    j=i+1
        ###    k=len(nums)-1
        ###    while j<k:
        ###        if nums[j]+nums[k] == target:
        ###            res.append([nums[i], nums[j], nums[k]])
        ###            j+=1
        ###            k-=1
        ###            while j<k and nums[j]==nums[j-1]:
        ###                j+=1
        ###            while j<k and nums[k]==nums[k+1]:
        ###                k-=1
        ###        elif nums[j]+nums[k] < target:
        ###            j+=1
        ###        else:
        ###            k-=1
        ###return res

# class Solution(object):
#     def threeSum(self, nums):
#         n = len(nums)
#         res = []
#         nums.sort()
        
#         for i in range(n-2):
#             if nums[i] + nums[i+1] + nums[i+2]>0:
#                 break
#             if nums[i] + nums[n-2] + nums[n-1]<0:
#                 continue
#             if i>0 and nums[i-1] == nums[i]:
#                 continue
#             left, right = i+1, n-1
#             while left<right:
#                 tmp = nums[i] + nums[left] + nums[right]
#                 if tmp == 0:
#                     res.append([nums[i], nums[left], nums[right]])
#                     while left+1<right and nums[left] == nums[left+1]:
#                         left += 1
#                     left += 1
#                     while left < right -1 and nums[right] == nums[right-1]:
#                         right -= 1
#                     right -=1
#                 elif tmp < 0:
#                     left += 1
#                 else:
#                     right -= 1
#         return res

import collections
class Solution(object):
    def threeSum(self, nums):  
        d = collections.defaultdict(list)
        comb = collections.deque()
        for i in range(len(nums)):
            d[nums[i]].append(i)
            for j in range(i+1, len(nums)):
                comb.append((- nums[i] - nums[j], i, j))

        res = list()
        for i in range(len(comb)):
            val, first, second = comb.popleft()
            if val in d:
                for v in d[val]:
                    if v != first and v != second:
                        third = v
                        tmp = sorted([nums[first], nums[second], nums[third]])
                        if tmp not in res:
                            res.append(tmp)
        return res

if __name__=="__main__":
    # nums=[-1, 0, 1, 2, -1, -4]
    # nums=[3,0,-2,-1,1,2]
    nums=[0,0,0,0]
    result = Solution().threeSum(nums)
    print(result)

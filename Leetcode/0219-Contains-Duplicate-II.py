class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        nums = [1,2,3,1], k = 3
        """
        ###d = {}
        ###for i in range(len(nums)):
        ###    d[nums[i]] = d.get(nums[i], []) + [i]
        ###    if len(d[nums[i]]) >= 2:
        ###        if d[nums[i]][-1] - d[nums[i]][-2] <= k:
        ###            return True
        ###return False
       
        ###d1 = {}
        ###for i, num in enumerate(nums):
        ###    if num in d1:
        ###        d1[num].append(i)
        ###    else:
        ###        d1[num] = [i]
        ###print(d1)
        ###for key, value in d1.items():
        ###    if len(value) >= 2:
        ###        pos1 = value[1:len(value)]
        ###        print(pos1)
        ###        pos2 = value[:-1]
        ###        print(pos2)
        ###        for i in range(len(pos1)):
        ###            print(i)
        ###            if pos1[i] - pos2[i] == k:
        ###                return True
        ###return False
        #
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = i
            else:
                if i - d[num] <= k:
                return True
                d[num] = i
        return False
        

if __name__ == '__main__':
    ###nums = [1, 2, 3, 1]
    ###k=3
    ###result = Solution().containsNearbyDuplicate(nums,k)
    ###print(result)
    
    ###nums = [1, 0, 1, 1]
    ###k = 1
    ###result = Solution().containsNearbyDuplicate(nums, k)
    ###print(result)
    
    nums = [99, 99]
    k=2
    result = Solution().containsNearbyDuplicate(nums,k)
    print(result)

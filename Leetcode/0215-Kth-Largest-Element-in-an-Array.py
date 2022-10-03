class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ###nums = sorted(nums)
        ###return nums[-k]
        
        from heapq import heappush, heappop
        
        heap = []
        for num in nums:
            heappush(heap, num)
        
        ordered = []
        while heap:
            ordered.append(heappop(heap))
        
        return ordered[-k]


def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        cnt = len(nums)
        while k < cnt:
            heapq.heappop(nums)
            cnt -= 1
        return nums[0]


class Solution(object):
    def findKthLargest(self, nums, k):
        tmp = sorted(nums)
        return tmp[-k]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def findKthLargestHelper(left, right, numberK):
            '''
                left will always be less than or equal right and 
                numberK will not exceed the value of right-left+1
            '''                
            pivot = nums[right]
            divider = left #all elements before divider are less than pivot
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[divider], nums[i] = nums[i], nums[divider]
                    divider += 1    
            nums[divider], nums[right] = nums[right], nums[divider]
            pivotIndex=divider

            if right - pivotIndex == numberK - 1:
                return nums[pivotIndex]
            elif right - pivotIndex < numberK - 1:
                return findKthLargestHelper(0, pivotIndex-1, numberK - (right - pivotIndex) - 1 )
            else:
                return findKthLargestHelper(pivotIndex+1, right, numberK)
            
        
        return findKthLargestHelper(0, len(nums)-1, k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
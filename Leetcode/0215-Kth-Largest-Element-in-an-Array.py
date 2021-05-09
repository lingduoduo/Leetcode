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
        while cnt > k:
            heapq.heappop(nums)
            cnt -= 1
        return nums[0]


class Solution(object):
    def findKthLargest(self, nums, k):
        tmp = sorted(nums)
        return tmp[-k]
import heapq

class Solution():
    def getMedian(self, nums):
        minnums = nums[:]
        heapq.heapify(minnums)
        maxnums = [-num for num in nums]
        heapq.heapify(maxnums)

        for i in range(len(nums)//2):
            min_num = heapq.heappop(minnums)
            max_num = - heapq.heappop(maxnums)
        return (min_num + max_num)/2 if len(nums) % 2 == 0 else heapq.heappop(minnums)

if __name__ == '__main__':
    res = Solution().getMedian([4, 5, 1, 6, 2, 7, 3, 8])
    print(res)
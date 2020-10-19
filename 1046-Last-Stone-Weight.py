import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        nums = [-stone for stone in stones]
        heapq.heapify(nums)
        
        while len(nums) >= 2:
            print(nums)
            first = -heapq.heappop(nums)
            second = -heapq.heappop(nums)
 
            if first > second:
                heapq.heappush(nums, -(first-second))
            
        return -nums[0] if nums else 0


        # stones = [-s for s in stones]
        # heapq.heapify(stones)
        # while len(stones) >= 2:
        #     s1 = heapq.heappop(stones)
        #     s2 = heapq.heappop(stones)
        #     if s1 != s2:
        #         heapq.heappush(stones, s1 - s2)
        # return -stones[0] if stones else 0

if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    results = Solution().lastStoneWeight(stones)
    print(results)
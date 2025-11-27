from typing import List
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = sorted(nums[::2])
        even = sorted(nums[1::2], reverse=True)
        res = []
        for i in range(len(even)):
            res.append(odd[i])
            res.append(even[i])
        if len(odd) > len(even):
            res.append(odd[-1]) 
        return res
            
if __name__ == "__main__":
    res = Solution().sortEvenOdd(nums = [4,1,2,3])
    res = Solution().sortEvenOdd(nums = [2, 1])
    print(res)
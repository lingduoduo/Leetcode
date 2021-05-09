class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        nums = [i for i in range(1, maxChoosableInteger+1)]
        if sum(nums) < desiredTotal:
            return False
        if sum(nums) == desiredTotal and len(nums) % 2 != 0:
            return True
       
        visited = {}

        def canwin(nums, target):
            if nums[-1] >= target:
                return True
            if tuple(nums) in visited:
                return visited[tuple(nums)]

            for i in range(len(nums)):
                if not canwin(nums[:i] + nums[i+1:], target-nums[i]):
                    visited[tuple(nums)] = True
                    return True
            visited[tuple(nums)] = False
            return False
   
        return canwin(nums, desiredTotal)
   
    
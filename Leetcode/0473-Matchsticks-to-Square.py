class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 4:
            return False
        
        tot = sum(nums)
        sub_tot = tot // 4
        if tot % 4 != 0 or max(nums) > sub_tot: 
            return False
        
        nums.sort(reverse = True)
        target = [0] * 4;
        
        def _dfs(index):
            if index == len(nums): 
                return True
            
            for i in range(4):
                if target[i] + nums[index] <= sub_tot:
                    target[i] += nums[index]
                    if _dfs(index + 1):
                        return True      
                    target[i] -= nums[index]
                    
            return False

        return _dfs(0)

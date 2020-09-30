class Solution:
    def trap(self, height: List[int]) -> int:
        leftmosthigh = [0 for i in range(len(height))]
        leftmax = 0
        for i in range(len(height)):
            if height[i] > leftmax: 
                leftmax = height[i]
            leftmosthigh[i] = leftmax
            
        res = 0
        rightmax = 0
        for i in reversed(range(len(height))):
            if height[i] > rightmax: rightmax = height[i]
            if min(rightmax, leftmosthigh[i]) > height[i]:
                res += min(rightmax, leftmosthigh[i]) - height[i]
        return res
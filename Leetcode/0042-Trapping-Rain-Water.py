# class Solution:
#     def trap(self, height: List[int]) -> int:
        # leftmosthigh = [0 for i in range(len(height))]
        # leftmax = 0
        # for i in range(len(height)):
        #     if height[i] > leftmax: 
        #         leftmax = height[i]
        #     leftmosthigh[i] = leftmax
            
        # res = 0
        # rightmax = 0
        # for i in reversed(range(len(height))):
        #     if height[i] > rightmax: rightmax = height[i]
        #     if min(rightmax, leftmosthigh[i]) > height[i]:
        #         res += min(rightmax, leftmosthigh[i]) - height[i]
        # return res


class Solution:
    def trap(self, height) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)
        for i in range(1, len(height)):
            leftmax[i] = max(leftmax[i-1], height[i-1])
        print(leftmax)
        for i in range(len(height)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i+1])
        print(rightmax)
        res = [0]*len(height)
        for i in range(len(height)):
            res[i] = max(0, min(leftmax[i], rightmax[i]) - height[i])
        return sum(res)

if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    results = Solution().trap(height)
    print(results)




class Solution:
    def maxArea(self, height) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        # first try
        # i=0
        # j=len(height)-1
        # result = 0
        # while i<j:
        #     result = max(result, (j-i)*min(height[i], height[j]))
        #     if height[i]<height[j]:
        #         i+=1
        #     else:
        #         j-=1
        # return result
        
        res = 0
        left = 0
        right = len(height)-1
        while left<right:
            h = min(height[left], height[right])
            res = max(res, h*(right-left))
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return res

if __name__=="__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))

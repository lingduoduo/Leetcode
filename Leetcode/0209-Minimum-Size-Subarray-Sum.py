class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        # if not nums: return 0
        # presum = []
        # presum.append(0)

        # for i in range(len(nums)):
        #     presum.append(presum[i] + nums[i])

        # print(presum)

        # res = float('inf')
        # for i in range(len(nums)):
        #     cnt = float('inf')
        #     for j in range(1,len(nums)+1):
        #         if presum[j] - presum[i] >= s:
        #             cnt = min(cnt, j-i)
        #             break
        #     res = min(res, cnt)
        # return 0 if res == float('inf') else res

        n= len(nums)
        left, right = 0, 0
        csum = 0
        res = float('inf')
        while right < n:
            csum += nums[right]
            while csum >= s:
                res = min(res, right - left + 1)
                csum -= nums[left]
                left += 1
            right += 1
        return res if res != float('inf') else 0

if __name__ == '__main__':
    # s=15
    # nums = [1,2,3,4,5]
    s = 7
    nums = [2,3,1,2,4,3]
    result = Solution().minSubArrayLen(s, nums)
    print(result)
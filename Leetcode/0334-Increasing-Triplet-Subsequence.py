class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3:
            return False

        # dp = [-1]*len(nums)
        # for i in range(len(nums)):
        #   j = i+1
        #   while j<len(nums):
        #       if nums[j]>nums[i]:
        #           dp[i] = j
        #           break
        #       j+=1
        # for i in range(len(nums)):
        #   cnt = 0
        #   j=i
        #   while dp[j]!=-1:
        #       j=dp[j]
        #       cnt += 1
        #       if cnt==2:
        #           return True
        # return False

        for i in range(1, len(nums) - 1):
            left = sum([1 for j in range(0, i) if nums[j] < nums[i]])
            right = sum([1 for j in range(i + 1, len(nums)) if nums[i] < nums[j]])
            if left >= 1 and right >= 1:
                return True
        return False


class Solution:
    def increasingTriplet(self, nums) -> bool:
        if len(nums) < 3:
            return False
        first, second = float("inf"), float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == "__main__":
    # nums = [1,2,3,4,5]
    # nums = [0, 4, 2, 1, 0, -1]
    nums = [5, 1, 5, 5, 2, 5, 4]
    results = Solution().increasingTriplet(nums)
    print(results)

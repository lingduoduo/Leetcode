class Solution:
    def findNumsAppearOnce(self, nums, target):
        res = []
        i = 0
        j = len(nums) - 1
        while i < j:
            cur = nums[i] + nums[j]
            if cur == target:
                return nums[i], nums[j]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return None

if __name__ == '__main__':
    nums = [1, 2, 4, 7, 11, 15]
    res = Solution().findNumsAppearOnce(nums, 15)
    print(res)
  

# ```java
# public ArrayList<Integer> FindNumbersWithSum(int[] nums, int target) {
#     int i = 0, j = nums.length - 1;
#     while (i < j) {
#         int cur = nums[i] + array[j];
#         if (cur == target)
#             return new ArrayList<>(Arrays.asList(nums[i], nums[j]));
#         if (cur < target)
#             i++;
#         else
#             j--;
#     }
#     return new ArrayList<>();

# ```
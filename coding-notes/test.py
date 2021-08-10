class Solution:
    def findNumsAppearOnce(self, nums):
        diff = 0
        for num in nums:
            diff ^= num 
        diff &= -diff

        res1 = 0 
        res2 = 0
        for num in nums:
            if num & diff == 0:
                res1 ^= num 
            else:
                res2 ^= num
        return sorted([res1, res2])
    
if __name__ == '__main__':
    nums = [2, 4, 3, 6, 3, 2, 5, 5]
    res = Solution().findNumsAppearOnce(nums)
    print(res)
  

# ```java
# public int[] FindNumsAppearOnce (int[] nums) {
#     int[] res = new int[2];
#     int diff = 0;
#     for (int num : nums)
#         diff ^= num;
#     diff &= -diff;
#     for (int num : nums) {
#         if ((num & diff) == 0)
#             res[0] ^= num;
#         else
#             res[1] ^= num;
#     }
#     if (res[0] > res[1]) {
#         swap(res);
#     }
#     return res;
# }

# private void swap(int[] nums) {
#     int t = nums[0];
#     nums[0] = nums[1];
#     nums[1] = t;

# ```
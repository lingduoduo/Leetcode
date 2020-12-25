class Solution:
    def totalHammingDistance(self, nums) -> int:
        res = 0
        mask = 1
        for i in range(32):
            cnt = 0
            for num in nums:
                if num & mask 



        return res


class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int ans = 0;
        int mask = 1;
        for (int i = 0; i < 32; ++i) {
            int count = 0;
            for (const int num : nums)
                if (num & mask) ++count;
            ans += (nums.size() - count) * count;
            mask <<= 1;
        }
        return ans;
    }
};


if __name__ == '__main__':
    nums = [4, 14, 2]
    res = Solution().totalHammingDistance(nums)
    print(res)
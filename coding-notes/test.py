class Solution():
    def getLeastNumbers_Solution(self, nums, k):
        res = []
        if k > len(nums) or k <= 0:
            return res

        self.findKthSmallest(nums, k - 1);
        for i in range(k):
            res.append(nums[i])
        return res

    def findKthSmallest(self, nums, k):
        l = 0
        r = len(nums) - 1
        while l < r:
            j = self.partition(nums, l, r)
            print(j)
            if j == k:
                break
            if j > k:
                r = j - 1
            else:
                l = j + 1

    def partition(self, nums, l, r):
        p = nums[l]
        i = l 
        j = r 
        while i < j:
            while i < r and nums[i] < p:
                i += 1
            while j > l and nums[j] > p:
                j -= 1
            if i == j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        return j 

if __name__ == '__main__':
    res = Solution().getLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], k=4)
    print(res)
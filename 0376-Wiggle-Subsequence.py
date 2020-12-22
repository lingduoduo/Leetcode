class Solution:
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums)
        if n <= 1:
            return n
            
        inc, dec = 1, 1
        for x in range(1, n):
            print([inc, dec])
            if nums[x] > nums[x - 1]:
                inc = dec + 1
            elif nums[x] < nums[x - 1]:
                dec = inc + 1
        return max(inc, dec)   	

if __name__ == '__main__':
	nums = [1,17,5,10,13,15,10,5,16,8]
	res = Solution().wiggleMaxLength(nums)
	print(res)
	
class Solution:
    def numSub(self, s: str) -> int:
        nums = s.split("0")
        res = 0
        for num in nums:
            res += len(num)*(len(num)+1)//2
        return res % 1000000007

if __name__ == '__main__':
	s = "1111111111011010011"
	results = Solution().numSub(s)
	print(results)
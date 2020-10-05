class Solution:
    def countSegments(self, s: str) -> int:
        if len(s)==0: return 0
        
        words = s.split(" ")
        return sum([1  for word in words if word != ""])

if __name__ == '__main__':
	s = "                "
	result = Solution().countSegments(s)
	print(result)
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)
        mid = n//2

        if n%2==0:
        	for i in range(n//2):
        		s[mid+i], s[mid-(i+1)] = s[mid-(i+1)], s[mid+i]
        else:
        	for i in range(1,n//2+1):
        		s[mid+i], s[mid-i] = s[mid-i], s[mid+i]
        print(s)

if __name__ == "__main__":
	input = ["h","e","l","l","o"]
	input = ["e","l","l","o"]
	result = Solution().reverseString(input)
	print(result)   

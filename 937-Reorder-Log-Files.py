class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = {}
        digits = []

        for log in logs:
        	items = log.split(" ")
        	if items[1][0].isalpha():
        		letters[" ".join(items[1:])] = log
        	else:
        		digits.append(log)
        letterKeys = sorted(letters.keys())
        return [letters[key] for key in letterKeys]+digits

if __name__ == "__main__":
	logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
	result = Solution().reorderLogFiles(logs)
	print(result)   

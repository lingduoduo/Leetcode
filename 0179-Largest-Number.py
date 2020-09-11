class compare(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums):
    	strs = [str(num) for num in nums]
    	largest = sorted(strs, key=compare)
    	largest = ''.join(largest)

    	return '0' if largest[0] == '0' else largest

# class Solution:
#     def largestNumber(self, nums):
#     	strs = [str(num) for num in nums]
#     	strs.sort(reverse=True)


    	# # largest = sorted(strs, key=compare)
    	# largest = ''.join(largest)

    	# return '0' if largest[0] == '0' else largest


if __name__=="__main__":
	result = Solution().largestNumber(nums=[3,30,34,5,9])
	print(result)

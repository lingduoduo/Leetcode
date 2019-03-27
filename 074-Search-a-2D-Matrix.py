class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nrow = len(matrix)
        ncol = len(matrix[0])

        left = 0
        right = nrow*ncol

        while left<right:

        	mid = left + (right-left)//2
        	# print([left, right, mid])

        	# if nrow==1:
        	# 	mid_value=matrix[0][mid]
        	# elif ncol==1:
        	# 	mid_value=matrix[mid][0]
        	# else:
        	mid_value=matrix[mid//ncol][mid%ncol]

        	if mid_value==target:
        		return True
        	elif mid_value<target:
        		left = mid+1
        	else:
        		right = mid

        return False

if __name__=="__main__":
    matrix = [[ 1,  5,  9],[10, 11, 12],[13, 13, 15]]
    result = Solution().searchMatrix(matrix, 1)
    print(result)
    result = Solution().searchMatrix(matrix, 15)
    print(result)
    result = Solution().searchMatrix(matrix, 4)
    print(result)
    matrix = [[ 1, 1]]
    result = Solution().searchMatrix(matrix, 0)
    print(result)
    matrix = [[1],[3]]
    result = Solution().searchMatrix(matrix, 3)
    print(result)
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    result = Solution().searchMatrix(matrix, 24)
    print(result)
class Solution:
    def trimMean(self, arr) -> float:
        arr.sort()
        print(len(arr))
        cnt = int(len(arr)*0.05) 
        res = arr[cnt:len(arr)-cnt]
        print(res)
        return sum(res)/len(res)

if __name__ == '__main__':
	# arr = list(range(1, 100))
	arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
	results = Solution().trimMean(arr)
	print(results)

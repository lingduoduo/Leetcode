
def twoSum(rawList, target):
	for k, v in enumerate(rawList):
		i = k+1
		while i<len(rawList):
			if v+rawList[i] == target:
				return([k, i])
			else:
				i=i+1
	return([])

if __name__=="__main__":
	numbers=[2, 7, 11, 15]
	results = twoSum(numbers, 9)
	print(results)

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA = sum(A)
        sumB = sum(B)
        setB = set(B)

        target = (sumA + sumB)//2
        res = []

        for a in A:
        	if target - (sumA - a) in setB:
        		res.append([a, target - (sumA - a)])
        return res

if __name__ == '__main__':
	A = [1,1]
	B = [2,2]
	res = Solution().fairCandySwap(A, B)
	print(res)
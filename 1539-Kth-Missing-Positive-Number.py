class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        n = len(arr)
        for i in range(n):
            while arr[i] != num and k != 0:
                result = num
                num += 1
                k -= 1
            if k == 0:
                return result
            else:
                num += 1
        
        result = num - 1
        while k>0:
            result += 1
            k -= 1


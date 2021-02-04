class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        strings = "123456789"
        start = len(str(low))
        end = len(str(high))
        while start <= end:
            for i in range(len(strings)-start+1):
                num = int(strings[i:i+start])
                if low <= num <= high:
                    res.append(num)
            start += 1
        return res
                
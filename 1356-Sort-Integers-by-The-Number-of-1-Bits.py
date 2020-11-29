import collections
class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1') << 16) + x)

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        for i in range(len(arr)):
            d[bin(arr[i]).count('1')].append(arr[i])
            d[bin(arr[i]).count('1')] = sorted(d[bin(arr[i]).count('1')])
        result = sorted(d.items(), key = lambda x: x[0])
        res = []
        for k, v in result:
            res.extend(v)
        return res
        
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        
        d = collections.defaultdict(list)
        
        for i in range(len(arr)):
            d[bin(arr[i]).count('1')].append(arr[i])

        result = sorted(d.items(), key = lambda x: x[0])
        res = []
        for k, v in result:
            res.extend(v)
        return res
            

if __name__ == '__main__':
	arr = [0,1,2,3,4,5,6,7,8]
	results = Solution().sortByBits(arr)
	print(results)
class Solution:
    def arrayRankTransform(self, arr):
        if not arr: return []
        sorted_orders = sorted(arr)
        j = 1
        d = {sorted_orders[0] : 1}
        res = []
        for i in range(1, len(sorted_orders)):
            j = len(d.keys())
            if sorted_orders[i] not in d:
                d[sorted_orders[i]] = j + 1

        for i in range(len(arr)):
            res.append(d[arr[i]])
            
        return res

if __name__ == '__main__':
    arr = [40,10,20,30]
    arr = [100,100,100]
    arr = [37,12,28,9,100,56,80,5,12]
    result = Solution().arrayRankTransform(arr)    
    print(result)
    
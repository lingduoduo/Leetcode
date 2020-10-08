class Solution:
    def arrayRankTransform(self, arr):
        sorted_orders = sorted(arr)
        print(sorted_orders)

        d = {}
        res = []

        i = 0
        while i < len(sorted_orders):
            if sorted_orders[i] not in d:
                d[sorted_orders[i]] = i + 1
                i += 1

        for i in range(len(arr)):
            res.append(d[arr[i]])
            
        return res

if __name__ == '__main__':
    arr = [37,12,28,9,100,56,80,5,12]
    [37,12,28,9,100,56,80,5,12]

[5,3,4,2,8,6,7,1,3]

    # [5, 9, 12, 12, 28, 37, 56, 80, 100]
    # # 
    # [5, 3, 4, 2, 8, 6, 7, 1, 3]
    # [6, 3, 5, 2, 9, 7, 8, 1, 3]
    result = Solution().arrayRankTransform(arr)    
    print(result)
    
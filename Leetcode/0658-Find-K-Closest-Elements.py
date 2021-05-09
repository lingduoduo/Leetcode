import heapq
class Solution:
    def findClosestElements(self, arr, k, x):
        stack = []
        heapq.heapify(stack)
        res = []
        for val in arr:
            stack.append((abs(x-val), val))
        ksmallest = heapq.nsmallest(k, stack)
        # print(ksmallest)
        for i in range(len(ksmallest)):
            res.append(ksmallest[i][1])
        return res

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    results = Solution().findClosestElements(arr, k, x)
    print(results)

# Input: 
# Output: [1,2,3,4]
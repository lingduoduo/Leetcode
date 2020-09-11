class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        ###d = dict()
        ###i = 0
        ###for point in points:
        ###    d[i] = point[0] ** 2 + point[1] ** 2
        ###    i += 1
        ###k = sorted(d.values())
        #
        ###result = list()
        ###for j in range(len(points)):
        ###    if d[j] <= k[K - 1]:
        ###        result.append(points[j])
        ###return result
        
        import heapq
        heap = []
        for p in points:
            d = p[0]**2 + p[1]**2
            heap.append([d, p])
        
        heapq.heapify(heap)
        res = []
        for d in heapq.nsmallest(K, heap):
            res.append(d[1])
        return res

if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    results = Solution().kClosest(points, K)
    print(results)

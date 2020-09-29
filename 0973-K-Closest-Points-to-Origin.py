# class Solution(object):
#     def kClosest(self, points, K):
        # """
        # :type points: List[List[int]]
        # :type K: int
        # :rtype: List[List[int]]
        # """
        # ###d = dict()
        # ###i = 0
        # ###for point in points:
        # ###    d[i] = point[0] ** 2 + point[1] ** 2
        # ###    i += 1
        # ###k = sorted(d.values())
        # #
        # ###result = list()
        # ###for j in range(len(points)):
        # ###    if d[j] <= k[K - 1]:
        # ###        result.append(points[j])
        # ###return result
        
        # # import heapq
        # # heap = []
        # # for p in points:
        # #     d = p[0]**2 + p[1]**2
        # #     heap.append([d, p])
        
        # # heapq.heapify(heap)
        # # res = []
        # # for d in heapq.nsmallest(K, heap):
        # #     res.append(d[1])
        # # return res

class Solution(object):
    def kClosest(self, points, K):
        dist = []
        for i in range(len(points)):
            x, y = points[i]
            dist.append(x**2 + y**2)

        prev = dist
        dist = sorted(dist)
        res = []
        for i in range(len(prev)):
            if prev[i] <= dist[K-1]:
                res.append(points[i])
        return res

class Solution(object):
    def kClosest(self, points, K):
        dist = []
        for i in range(len(points)):
            x, y = points[i]
            dist.append(((x**2 + y**2), (x,y)))

        heapq.heapify(dist)
        res = []
        nsmallest = heapq.nsmallest(K, dist)
        for dist, point in nsmallest:
            res.append(point)
        return res


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    results = Solution().kClosest(points, K)
    print(results)

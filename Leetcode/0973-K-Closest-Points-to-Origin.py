class Solution(object):
    def kClosest(self, points, K):
        dist = []
        for i in range(len(points)):
            x, y = points[i]
            dist.append(x ** 2 + y ** 2)

        prev = dist
        dist = sorted(dist)
        res = []
        for i in range(len(prev)):
            if prev[i] <= dist[K - 1]:
                res.append(points[i])
        return res


class Solution(object):
    def kClosest(self, points, K):
        dist = []
        for i in range(len(points)):
            x, y = points[i]
            dist.append(((x ** 2 + y ** 2), (x, y)))

        heapq.heapify(dist)
        res = []
        nsmallest = heapq.nsmallest(K, dist)
        for dist, point in nsmallest:
            res.append(point)
        return res


class Solution(object):
    def kClosest(self, points, K):
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    results = Solution().kClosest(points, K)
    print(results)

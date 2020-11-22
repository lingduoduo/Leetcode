import collections
class Solution:
    def largestOverlap(self, img1, img2) -> int:
        N = len(img1)
        LA = [(xi, yi) for xi in range(N) for yi in range(N) if img1[xi][yi]]

        LB = [(xi, yi) for xi in range(N) for yi in range(N) if img2[xi][yi]]

        d = collections.Counter([(x1 - x2, y1 - y2) for (x1, y1) in LA for (x2, y2) in LB])

        return max(d.values() or [0])

if __name__ == '__main__':
	img1 = [[1,1,0],[0,1,0],[0,1,0]]
	img2 = [[0,0,0],[0,1,1],[0,0,1]]
	res = Solution().largestOverlap(img1, img2)
	print(res)
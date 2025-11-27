class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = dict()
        res = 0
        for i in range(len(wall)):
            left = 0
            for j in range(len(wall[i]) - 1):
                left += wall[i][j]
                d[left] = d.get(left, 0) + 1
                res = max(res, d[left])
        return len(wall) - res


if __name__ == "__main__":
    walls = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    ###walls = [[1, 2, 2, 1],[3, 1, 2]]
    result = Solution().leastBricks(walls)
    print(result)

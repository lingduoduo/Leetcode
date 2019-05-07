class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
      # Method 1
        if image[sr][sc] == newColor:
            return image

        n = image
        m = image[0]
        oldColor = image[sr][sc]

        def Fill(x, y):
            if x <= 0 or x >= n or y <= 0 or y >= m:
                return
            if image[x][y] != oldColor:
                return
            image[x][y] = newColor
            Fill(x + 1, y)
            Fill(x - 1, y)
            Fill(x, y - 1)
            Fill(x, y + 1)

        Fill(sr, sc)
        return image

      # Method 2
        if image[sr][sc] == newColor:
            return image

        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image

    def dfs(self, image, sr, sc, oldColor, newColor):
        if image[sr][sc] == oldColor:
            image[sr][sc] = newColor
            print([sr, sc])
            if sr >= 1:
                self.dfs(image, sr - 1, sc, oldColor, newColor)
            if sr <= len(image) - 2:
                self.dfs(image, sr + 1, sc, oldColor, newColor)
            if sc >= 1:
                self.dfs(image, sr, sc - 1, oldColor, newColor)
            if sc <= len(image[0]) - 2:
                self.dfs(image, sr, sc + 1, oldColor, newColor)


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    result = Solution().floodFill(image, sr, sc, newColor)
    print(result)

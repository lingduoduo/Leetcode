class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        if image[sr][sc] == newColor:
            self.dfs(image, sr, sc, newColor)
        return image

    def dfs(self, image, sr, sc, newColor):
        if image[sr][sc] == newColor:
            return

        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            ssr = sr + direction[0]
            ssc = sc + direction[1]
            if (
                ssr < 0
                or ssr >= len(image)
                or ssc < 0
                or ssc >= len(image[0])
                or image[ssr][ssc] != oldColor
            ):
                continue
            self.dfs(image, ssr, ssc, newColor)


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    result = Solution().floodFill(image, sr, sc, newColor)
    print(result)

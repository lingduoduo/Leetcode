class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
        	return image

        n = image
        m = image[0]
        oldColor = image[sr][sc]

        def Fill(x, y):
	    	if x<=0 or x>=n or y<=0 or y>=m: return
	    	if image[x][y] !=  oldColor: return
	    	image[x][y] = newColor
            Fill(x+1, y)
            Fill(x-1, y)
            Fill(x, y-1)
            Fill(x, y+1)

        Fill(sr, sc)
        return image
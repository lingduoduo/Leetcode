class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # res = 0
        # for i in range(len(points)):
        #     d = dict()
        #     for j in range(len(points)):
        #         dist = (points[i][0] - points[j][0]) ** 2 + \
        #                (points[i][1] - points[j][1]) ** 2
        #         if dist in d:
        #             d[dist] += 1
        #         else:
        #             d[dist] = 1
        #     res += sum(v * (v - 1) for v in d.values())
        # return res
        res = 0
        
        for x1, x2 in points:
            d = {}
            for y1, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                
                distance = (x1 - x2)** 2 + (y1 - y2)**2
                print(distance)
                
                # if distance in d:
                #     res += d[distance]
                #     d[distance] += 1
                # else:
                #     d[distance] = 1
                    
        return 2*res


if __name__ == "__main__":
    numbers = [[0, 0], [1, 0], [2, 0]]
    # numbers = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
    result = Solution().numberOfBoomerangs(numbers)
    print(result)

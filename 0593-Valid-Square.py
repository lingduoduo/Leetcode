import collections
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        d = collections.defaultdict(int)
        l = [p1, p2, p3, p4]
        
        for i in range(len(l)-1):
            for j in range(i+1, len(l)):
                x0, y0 = l[i]
                x1, y1 = l[j]
                if (x0-x1)**2+ (y0-y1)**2 == 0:
                    return False
                else:
                    d[(x0-x1)**2+ (y0-y1)**2] += 1
                    
        if sorted(d.values()) == [2, 4]:
            return True
        else:
            return False

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dis = []
        dis.append((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        dis.append((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2)
        dis.append((p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2)
        dis.append((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2)
        dis.append((p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2)
        dis.append((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2)
        dis.sort()
        return dis[0] != 0 and dis[0] == dis[1] == dis[2] == dis[3] and dis[4] == dis[5]

if __name__ == '__main__':
    p1 = [0,0]
    p2 = [1,1]
    p3 = [1,0]
    p4 = [0,1]
    res = Solution().validSquare(p1, p2, p3, p4)
    print(res)

    p1 = [0,0]
    p2 = [1,1]
    p3 = [0,0]
    p4 = [1,1]
    res = Solution().validSquare(p1, p2, p3, p4)
    print(res)
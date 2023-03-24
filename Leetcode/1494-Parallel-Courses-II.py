from collections import deque
from itertools import combinations
class Solution(object):
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        pre = [0]*n
        occupy = [20]*(1<<(n))
        for dep in relations:
            pre[dep[1]-1] += 1<<(dep[0]-1)
        queue = deque([[0,0]])
        while queue:
            [num,step] = queue.popleft()
            nextlist = []
            for i in range(n):
                if pre[i]&num != pre[i]: continue
                if (1<<i)&num: continue
                nextlist.append(i)
            if len(nextlist)<=k:
                for ele in nextlist: num += 1<<ele
                if num+1==1<<n: return step+1
                if occupy[num]>step+1:
                    queue.append([num,step+1])
                    occupy[num] = step+1
            else:
                thelist = combinations(nextlist,k)
                for seq in thelist:
                    temp = num
                    for ele in list(seq): temp += 1<<ele
                    if occupy[temp]>step+1:
                        queue.append([temp,step+1])
                        occupy[temp] = step + 1
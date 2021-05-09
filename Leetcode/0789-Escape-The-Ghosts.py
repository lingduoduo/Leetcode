from typing import List
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mht = sum(map(abs, target))
        tx, ty = target
        return not any(abs(gx - tx) + abs(gy - ty) <= mht for gx, gy in ghosts)

if __name__ == '__main__':
	ghosts = [[1,0],[0,3]]
	target = [1,1]
	res = Solution().escapeGhosts(ghosts, target)
	print(res)
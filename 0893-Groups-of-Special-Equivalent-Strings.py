from typing import List
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        B = set()
        for a in A:
            B.add(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])))
            print(B)
        return len(B)

if __name__ == '__main__':
	A = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
	res = Solution().numSpecialEquivGroups(A)
	print(res)
	
import collections
class Solution:
    def repeatedNTimes(self, A) -> int:
        # cnt = collections.Counter(A)
        # return cnt.most_common(1)[0][0]

class Solution:
    def repeatedNTimes(self, A) -> int:
        visited = set()
        for num in A:
            if num not in visited:
                visited.add(num)
            else:
                return num

if __name__ == '__main__':
	A = [1,2,3,3]
	res = Solution().repeatedNTimes(A)
	print(res)
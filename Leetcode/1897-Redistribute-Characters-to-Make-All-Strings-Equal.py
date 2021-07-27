from typing import List
from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        strs = "".join(words)
        cnt = Counter(strs)

        for v in cnt.values():
            if v % len(words) != 0:
                return False
        return True
        
if __name__ == '__main__':
    res = Solution().makeEqual(words=["abc","aabc","bc"])
    print(res)

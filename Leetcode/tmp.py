from typing import List, Optional
import heapq

import collections

class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = collections.Counter(word)

        f = collections.Counter(d.values())

        l = len(f)
        if l >= 3:
            return False

        if l == 1:
            if len(d.keys()) == 1:
                return True
            
            return list(f.keys())[0] == 1
        
        for v, freq in f.items():
            if v == 1 and freq == 1:
                return True

        values = list(f.keys())
        if values[0] - values[1] == 1 and f[values[0]] == 1:
            return True

        if values[1] - values[0] == 1 and f[values[1]] == 1:
            return True
        
        return False

# Test the code        
if __name__ == '__main__':
    res = Solution().equalFrequency("abcc")
    print(res)
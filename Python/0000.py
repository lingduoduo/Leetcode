from typing import List, Optional
from collections import deque, defaultdict
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur= [], []

        for word in words:
            strs = ' '.join(cur)
            if len(strs) + len(word) < maxWidth:
                cur.append(word)
            else:
                res.append(strs + ' ' * (maxWidth - len(strs)))
                cur = [word]

        strs = ' '.join(cur)        
        res.append(strs + ' ' * (maxWidth - len(strs)))     
        
        return res

if __name__ == "__main__":
    print(Solution().fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
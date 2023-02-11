9/1/2022

1762 - Buildings With an Ocean View
314	- Binary Tree Vertical Order Traversal
1570 - Dot Product of Two Sparse Vectors

1249 - Minimum Remove to Make Valid Parentheses	
408	- Valid Word Abbreviation
1650 - Lowest Common Ancestor of a Binary Tree III

680	- Valid Palindrome II	
249	- Group Shifted Strings
71	- Simplify Path	

65	- Valid Number	
708	- Insert into a Sorted Circular Linked List
921	- Minimum Add to Make Parentheses Valid

1091 - Shortest Path in Binary Matrix	
2060	- Check if an Original String Exists Given Two Encoded Strings	
236	- Lowest Common Ancestor of a Binary Tree	

227	- Basic Calculator II	
215	- Kth Largest Element in an Array	
339	- Nested List Weight Sum

301	- Remove Invalid Parentheses	
1216 - Valid Palindrome III
346	- Moving Average from Data Stream

938	- Range Sum of BST	
791 - Custom Sort String	
691	- Stickers to Apell Word

987	- Vertical Order Traversal of a Binary Tree	
636	- Exclusive Time of Functions	
162	- Find Peak Element

199	- Binary Tree Right Side View	
523	- Continuous Subarray Sum	
1891 - Cutting Ribbons

10/1/2022

56	- Merge Intervals	
973	- K Closest Points to Origin	
1428	- Leftmost Column with at Least a One

827	- Making A Large Island	
138	- Copy List with Random Pointer	
50 -	Pow(x, n)	

498	- Diagonal Traverse	
163	- Missing Ranges
689 - Maximum Sum of 3 Non-Overlapping Subarrays

129	- Sum Root to Leaf Numbers	
670	- Maximum Swap
560	- Subarray Sum Equals K	

416	- Partition Equal Subset Sum	
426	- Convert Binary Search Tree to Sorted Doubly Linked List
1123	- Lowest Common Ancestor of Deepest Leaves

529	- Minesweeper
825	- Friends Of Appropriate Ages	
347	- Top K Frequent Elements	

173	- Binary Search Tree Iterator	
489	- Robot Room Cleaner
125	- Valid Palindrome

1340 - Jump Game V
543	- Diameter of Binary Tree	
766 - Toeplitz Matrix	

779	- K-th Symbol in Grammar	
958	- Check Completeness of a Binary Tree
1004 - Max Consecutive Ones III

271	- Encode and Decode Strings
298	- Binary Tree Longest Consecutive Sequence
1192	- Critical Connections in a Network	

11/1/2022

1644	- Lowest Common Ancestor of a Binary Tree II
939	- Minimum Area Rectangle	
1424	- Diagonal Traverse II	

2210 - Count Hills and Valleys in an Array
266- Palindrome Permutation
528 - Random Pick with Weight	

270	- Closest Binary Search Tree Value
415	- Add Strings	
88 - Merge Sorted Array	

953	- Verifying an Alien Dictionary	
398	- Random Pick Index	
31	- Next Permutation	

159 - Lingest Substring with At Most Two Distinct Characters
1047 - Remove All Adjacent Duplicates In String	
1539 - Kth Missing Positive Number	

1060 - Missing Element in Sorted Array
161	- One Edit Distance
146	- LRU Cache	

78	- Subsets	
977	- Squares of a Sorted Array	
23	- Merge k Sorted Lists	

2024	- Maximize the Confusion of an Exam	
1209	- Remove All Adjacent Duplicates in String II	
34	- Find First and Last Position of Element in Sorted Array	

896	- Monotonic Array	
623	- Add One Row to Tree
824	- Goat Latin	

779	- K-th Symbol in Grammar	
246	- Strobogrammatic Number

863	- All Nodes Distance K in Binary Tree	
583	- Delete Operation for Two Strings
1213	- Intersection of Three Sorted Arrays

319	- Bulb Switcher	
266	- Palindrome Permutation
463	- Island Perimeter

378	- Kth Smallest Element in a Sorted Matrix	
139	- Word Break	
283	- Move Zeroes

### 3Sum

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur < 0:
                    j += 1
                elif cur > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j += 1
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res
```

### 3Sum Closest

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cur = None
        gap = 10000000
        for i in range(len(nums)):
            if cur == nums[i]:
                i += 1
                continue
            cur = nums[i]
            j = i + 1
            k = len(nums) -1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k] - target
                gap = tmp if abs(tmp) < abs(gap) else gap
                if tmp > 0:
                    k -= 1
                elif tmp < 0:
                    j += 1
                else:
                    return target
        return target + gap
```

### Accounts Merge

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        edge = defaultdict(list)
        names = {}
        for account in accounts:
            for i in range(1, len(account)-1):
                email, nemail = account[i], account[i + 1]
                edge[email].append(nemail)
                edge[nemail].append(email)
            names[account[-1]] = account[0]
        
        visited = set()
        res = []
        for email, name in names.items():
            if email not in visited:
                emails = [email]
                visited.add(email)
                q = [email]
                while q:
                    e = q.pop()
                    for neighbor in edge[e]:
                        if neighbor not in visited:
                            emails.append(neighbor)
                            visited.add(neighbor)
                            q.append(neighbor)
                emails.sort()
                res.append([name] + emails)
        return res
```

### Add Strings

```python
class Solution(object):
    def addStrings(self, num1, num2):
        res = []
        c = 0
        l1 = len(num1)
        l2 = len(num2)
        while l1 or l2 or c:
            if l1:
                l1 -= 1
                c += int(num1[l1])
            if l2:
                l2 -= 1
                c += int(num2[l2])
            res.append(str(c % 10))
            c /= 10
        return ''.join(reversed(res))
```

### Alien Dictionary

```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        edge = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in edge[c]:
                        edge[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word): 
                    return ""
        res = []
        q = deque([c for c in in_degree if in_degree[c] == 0])
        while q:
            cur = q.popleft()
            res.append(cur)
            for d in edge[cur]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    q.append(d)
        if len(res) < len(in_degree):
            return ""
        return "".join(res)
```

### Angle Between Hands of a Clock

```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = 5.5 * (hour * 60 + minutes) % 360
        return angle if angle <= 180 else 360 - angle
```

### floating strings相加

```python

```

### Appear Times

```python
import bisect
def appear_times(num, target):
    left = bisect.bisect_left(num, target)
    right = bisect.bisect_right(num, target)
    return right - left
```

### atoi

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        flag = 1
        if s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        res = 0
        for c in s:
            if not c.isdigit():
                break
            res *= 10
            res += ord(c) - ord('0')
            if flag == 1:
                if res > 2147483647:
                    return INT_MAX
            else:
                if res > 2147483648:
                    return INT_MIN
        return res * flag
```

### Balance a Binary Search Tree

```python
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        dummy.right = root
        self.recBalance(root, dummy)
        return dummy.right
        
    def rotateLeft(self, root, parent):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        
        if parent.left == root:
            parent.left = new_root
        else:
            parent.right = new_root
        return new_root
    
    def rotateRight(self, root, parent):
        new_root = root.left 
        root.left = new_root.right 
        new_root.right = root
        
        if parent.left == root:
            parent.left = new_root
        else:
            parent.right = new_root
        return new_root
    
    def recBalance(self, node, parent):
        if not node:
            return 0, 0
        left_height, left_balance = self.recBalance(node.left, node)
        right_height, right_balance = self.recBalance(node.right, node)
        node_balance = left_height - right_height
        if node_balance > 1:
            if left_balance < 0:
                self.rotateLeft(node.left, node)
            return self.recBalance(self.rotateRight(node, parent), parent)
        elif node_balance < -1:
            if right_balance > 0:
                self.rotateRight(node.right, node)
            return self.recBalance(self.rotateLeft(node, parent), parent)
        else:
            return max(left_height, right_height) + 1, left_height - right_height
```

```python
class Solution:
	def balanceBST(self, root: TreeNode) -> TreeNode:
		v = []
		def dfs(node):
			if node:
				dfs(node.left)
				v.append(node.val)
				dfs(node.right)
		dfs(root)

		def bst(v):
			if not v:
				return None
			mid = len(v) // 2
			root = TreeNode(v[mid])
			root.left = bst(v[:mid])
			root.right = bst(v[mid + 1:])
			return root

		return bst(v)
```

### Basic Calculator II

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack, cur, op = [], 0, '+'
        for c in s + '+':
            if c == " ":
                continue
            if c.isdigit():
                cur = (cur * 10) + int(c)
            else:
                if op == '-':
                    stack.append(-cur)
                elif op == '+':
                    stack.append(cur)
                elif op == '*':
                    stack.append(stack.pop() * cur)
                elif op == '/':
                    stack.append(int(stack.pop() / cur))
                cur, op = 0, c
        return sum(stack)
```

### Binary Search Tree Iterator

```python
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
            
    def next(self) -> int:
        ret = self.stack.pop()
        node = ret.right
        while node:
            self.stack.append(node)
            node = node.left
        return ret.val

    def hasNext(self) -> bool:
        return self.stack
```

### Binary Tree Level Order Traversal

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = [root]
        while q:
            res.append([node.val for node in q])
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
        return res
```

### Binary Tree Maximum Path Sum

```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def traversal(root):
            if root is None:
                return 0
            left = max(0, traversal(root.left))
            right = max(0, traversal(root.right))
            self.res = max(self.res, left + right + root.val)
            return max(left, right, 0) + root.val

        self.res = float("-inf")
        traversal(root)
        return self.res
```

### Binary Tree Right Side View

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, max_depth = {}, 0
        stack = [(root, 0)]
        while stack:
            cur, depth = stack.pop()
            max_depth = max(max_depth, depth)
            res.setdefault(depth, cur.val)
            if cur.left:
                stack.append((cur.left, depth + 1))
            if cur.right:
                stack.append((cur.right, depth + 1))
        return [res[depth] for depth in range(max_depth + 1)]
```

### Binary Tree Vertical Order Traversal

```python
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = {}
        q = deque([(root, 0)])
        while len(q) > 0:
            n, pos = q[0]
            q.popleft()
            res.setdefault(pos, [])
            res[pos].append(n.val)
            if n.left != None:
                q.append( (n.left, pos - 1) )
            if n.right != None:
                q.append( (n.right, pos + 1) )
                
        keys = res.keys()
        minn = min(keys)
        maxx = max(keys)
        
        ret = []
        for i in range(minn, maxx + 1):
            ret.append(res[i])
        return ret
```

### Convert Binary Search Tree to Sorted Doubly Linked List

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            nonlocal last, first
            if node:
                dfs(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node        
                last = node
                dfs(node.right)
        if not root:
            return None
        first, last = None, None
        dfs(root)
        last.right = first
        first.left = last
        return first
```

### Combinations

```python
class Solution(object):
    def com(self, l, n, d, k):
        if d == k:
            return [[l]]
        res = []
        for i in range(l+1, n + 1 - (k - d - 1)):
            tmp = self.com(i, n, d + 1, k)
            if l == 0:
                res += tmp
            else:
                for p in tmp:
                    res.append([l] + p)
        return res
        
    def combine(self, n, k):
        return self.com(0, n, 0, k)
```

### check if string is parlindrome, ignore non a-z A-Z chars

```python

```

### Data Stream as Disjoint Intervals

```python

```

### Design Skiplist

```python
class Node:
    __slots__ = 'val', 'levels'
    def __init__(self, val, levels):
        self.val = val
        self.levels = [None] * levels

class Skiplist(object):
    def __init__(self):
        self.head = Node(-1, 16) 
    
    def _iter(self, num):
        cur = self.head
        for level in range(15, -1, -1):
            while True:
                future = cur.levels[level]
                if future and future.val < num:
                    cur = future
                else:
                    break
            yield cur, level

    def search(self, target):
        for prev, level in self._iter(target):
            pass
        cur = prev.levels[0]
        return cur and cur.val == target

    def add(self, num):
        nodelvls = min(16, 1 + int(math.log2(1.0 / random.random())))
        node = Node(num, nodelvls)
        
        for cur, level in self._iter(num):
            if level < nodelvls:
                future = cur.levels[level]
                cur.levels[level] = node
                node.levels[level] = future

    def erase(self, num):
        ans = False
        for cur, level in self._iter(num):
            future = cur.levels[level]
            if future and future.val == num:
                ans = True
                cur.levels[level] = future.levels[level]
        return ans
```

### Design TicTacToe

```python
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.xcol = [0 for i in range(n)]
        self.xrow = [0 for i in range(n)]
        self.xd1 = 0
        self.xd2 = 0
        self.ycol = [0 for i in range(n)]
        self.yrow = [0 for i in range(n)]
        self.yd1 = 0
        self.yd2 = 0
        self.n = n
        
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            n = self.n
            self.xcol[col] += 1
            if self.xcol[col] == n:
                return 1
            self.xrow[row] += 1
            if self.xrow[row] == n:
                return 1
                
            if col == row:
                self.xd1 += 1
            if n - row - 1 == col:
                self.xd2 += 1
            
            if self.xd1 == n:
                return 1
            if self.xd2 == n:
                return 1
                
        if player == 2:
            n = self.n
            self.ycol[col] += 1
            if self.ycol[col] == n:
                return 2
            self.yrow[row] += 1
            if self.yrow[row] == n:
                return 2
            if col == row:
                self.yd1 += 1
            if n - row - 1 == col:
                self.yd2 += 1
            if self.yd1 == n:
                return 2
            if self.yd2 == n:
                return 2
        return 0
```

### Divide Two Integers

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        maxint = 2147483647
        sign = (dividend < 0) == (divisor < 0)
        if divisor == 0:
            return maxint
        if dividend == 0:
            return 0
        divisor, dividend = abs(divisor), abs(dividend)
        res = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                tmp <<= 1
                i <<= 1
        if not sign:
            res = -res
        return min(max(res, -maxint-1), maxint)
```

### FB Sticker

```python
from collections import Counter
import math

def fb_sticker(target):
    dic = {'f': 1, 'a': 1, 'c': 1, 'e': 1, 'b': 1, 'o': 2, 'k': 1}
    res = 0
    for k, v in Counter(target).items():
        if k not in dic:
            continue
        res = max(res, math.ceil(v/dic[k]))
    return res
```

### Find Peak Element

```python
class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                return l
            m = (l + r) / 2
            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
```

### Group Shifted Strings

```python
class Solution(object):
    def convert(self, s):
        if len(s) == 1:
            return tuple()
        ret = []
        for i in range(1, len(s)):
            t = ord(s[i]) - ord(s[i - 1])
            ret.append(t if t > 0 else t + 26)
        return tuple(ret)
                
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strings:
            t = self.convert(s)
            dic.setdefault(t, [])
            dic[t].append(s)
        res = []
        for key in dic:
            res.append(dic[key])
        return res
```

### Implement getlast map

```python
class newDS:
    def __init__(self):
        self.hmap = collections.OrderedDict()
    def get(self, key):
        if key in self.hmap:
            return self.hmap[key]
        return -1
    def add(self, key, val):
        self.hmap[key] = val
    def remove(self, key):        
        if key in self.hmap:
            self.hmap.move_to_end(key)
            self.hmap.popitem()
    def getLast(self):
        if not self.hmap:
            return -1        
        key,val = self.hmap.popitem()
        self.hmap[key] = val
        return val
```

### Interval Overlap

```python

```

### find all local peaks and valleys

```python

```

### Find First and Last Position of Element in Sorted Array

```python
class Solution:
    def searchRange(self, nums, target):
      def search(n):
          lo, hi = 0, len(nums)
          while lo < hi:
              mid = (lo + hi) / 2
              if nums[mid] >= n:
                  hi = mid
              else:
                  lo = mid + 1
          return lo
    lo = search(target)
    return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]
```

### left most colume have 1

```python
import bisect
def left_most(A):
    m, cur = len(A), len(A[0]) - 1
    f = False
    for i in range(m):
        if A[i][cur] == 0:
            continue
        f = True
        cur = bisect.bisect_left(A[i], 1, 0, cur)
    return cur if f else -1
```

### Koko Eating Bananas

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(n):
            t = 0
            for p in piles:
                t += p // n
                t += p % n != 0
            return t <= h
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
```

### K Closest Points to Origin

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for px, py in points:
            t = (-(px * px + py * py), px, py)
            if len(q) < k:
                heapq.heappush(q, t)
            else:
                heapq.heappushpop(q, t)
        return [[p[1], p[2]] for p in q]
```

### Knight Dialer

```python
class Solution:
    def knightDialer(self, N: int) -> int:
        dic = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        M = 10**9 + 7
        dp = [1] * 10
        for k in range(N - 1):
            tdp = [0] * 10
            for i, j in enumerate(dp):
                for n in dic[i]:
                    tdp[n] += j
                    tdp[n] %= M
            dp = tdp
        return sum(dp) % M
```

### Kth Largest Element in an Array

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        def quickSelect(nums, l, r, k):
            i, j, pivot = l, r, nums[r]
            while i < j:
                if nums[i] > pivot:
                    j -= 1
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            m = i - l + 1
            if m == k:
                return i
            elif m > k:
                return quickSelect(nums, l, i - 1, k)
            else:
                return quickSelect(nums, i + 1, r, k - m)
        
        n = len(nums)
        return nums[quickSelect(nums, 0, n - 1, n - k + 1)]
```

### Kth Smallest Element in a BST

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
```

### LRU Cache

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.OrderedDict()
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:
            if self.size < self.capacity:
                self.dict[key] = value
                self.size += 1
            else:
                self.dict.popitem(False)
                self.dict[key] = value
```

### Local Minima

```python
def localMinUtil(arr, low, high, n):
    mid = low + (high - low) // 2  
    if(mid == 0 or arr[mid - 1] > arr[mid] and
       mid == n - 1 or arr[mid] < arr[mid + 1]):
        return mid
    elif(mid > 0 and arr[mid - 1] < arr[mid]):
        return localMinUtil(arr, low, mid - 1, n)
    return localMinUtil(arr, mid + 1, high, n)

def localMin(arr, n):
    return localMinUtil(arr, 0, n - 1, n)
```

### Longest Increasing Path in a Matrix

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(x, y):
            val = matrix[x][y]
            ret = 1 + max(
                dp(x - 1, y) if x > 0 and val > matrix[x - 1][y] else 0,
                dp(x + 1, y) if x < m - 1 and val > matrix[x + 1][y] else 0,
                dp(x, y - 1) if y > 0 and val > matrix[x][y - 1] else 0,
                dp(x, y + 1) if y < n - 1 and val > matrix[x][y + 1] else 0)
            return ret
            
        m, n = len(matrix), len(matrix[0])
        return max(dp(x, y) for x in range(m) for y in range(n))
```

### Longest Substring with At Most K Distinct Characters

```python
from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0 or n == 0:
            return 0
        left, right = 0, 0
        dic = OrderedDict()
        res = 1
        while right < n:
            character = s[right]
            if character in dic:
                del dic[character]
            dic[character] = right
            right += 1
            if len(dic) == k + 1:
                _, del_idx = dic.popitem(last = False)
                left = del_idx + 1
            res = max(res, right - left)
        return res
```

### Lowest Common Ancestor of a Binary Tree III

```python
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()
        while p:
            path.add(p)
            p = p.parent 
        while q not in path:
            q = q.parent 
        return q
```

### Making A Large Island

```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ret = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ret += dfs(nr, nc, index)
            return ret

        area = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        res = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    res = max(res, 1 + sum(area[i] for i in seen))
        return res
```

### max depth of parentheses of expression

```python

```

###  Max Stack

```python
class MaxStack:
    def __init__(self):
        self.s = []
    def push(self, x: int) -> None:
        m = max(x, self.s[-1][1] if self.s else x)
        self.s.append((x, m))
    def pop(self) -> int:
        return self.s.pop()[0]
    def top(self) -> int:
        return self.s[-1][0]
    def peekMax(self) -> int:
        return self.s[-1][1]
    def popMax(self) -> int:
        m = self.s[-1][1]
        b = []
        while self.s[-1][0] != m:
            b.append(self.s.pop()[0])
        self.pop()
        for it in b[::-1]:
            self.push(it)
        return m
```

### Meeting Rooms

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
```

### Meeting Rooms II

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        for i in intervals:
            if heap and i[0] >= heap[0]: 
                heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])
        return len(heap)
```

### Merge k Sorted Lists

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next
        res = ListNode()
        cur = res
        while q:
            val, i = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next
        return res.next
```

### Merge Intervals

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res
```

### Merge Sorted Array

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i, k = i - 1, k - 1
            else:
                nums1[k] = nums2[j]
                j, k = j - 1, k - 1
        while j >= 0:
            nums1[k] = nums2[j]
            j, k = j - 1, k - 1
```

### Minimum Add to Make Parentheses Valid

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = bal = 0
        for c in s:
            if c == "(":
                bal += 1
            elif bal:
                bal -= 1
            else:
                res += 1
        return res + bal
```

### Minimum Remove to Make Valid Parentheses

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ct = 0
        res = []
        for c in s:
            if c == '(':
                ct += 1
                res.append(c)
            elif c == ')':
                if ct > 0:
                    ct -= 1
                    res.append(c)
            else:
                res.append(c)
        for i in range(len(res)-1, -1, -1):
            if ct == 0:
                break
            if res[i] == "(":
                ct -= 1
                res[i] = ""
        return ''.join(res)
```

### Minimum Cost For Tickets

```python
# dp[i]表示车票覆盖到第i天的最小花费,dp[last_day]为所求
# dp[0] = 0
# dp[i] = min dp[i - 1] + costs[0] if i - 1 > 0 else costs[0]
#             dp[i - 7] + costs[1] if i - 7 > 0 else costs[1]
#             dp[i - 30] + costs[2] if i - 30 > 0 else costs[2]
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        first, last = days[0], days[-1]
        days = set(days)
        dp = [0] * (last + 1)
        for i in range(first, last + 1):
            if i in days:
                p1 = dp[i - 1] if i - 1 > 0 else 0
                p7 = dp[i - 7] if i - 7 > 0 else 0
                p30 = dp[i - 30] if i - 30 > 0 else 0
                dp[i] = min(p1 + costs[0], p7 + costs[1], p30 + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[last]
```

### Minimum Window Substring

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = j = I = J = 0
        miss = len(t)
        need = collections.Counter(t)
        for c in s:
            j += 1
            if need[c] > 0:
                miss -= 1
            need[c] -= 1
            if miss == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if J == 0 or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
```

### Missing Number

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) + 1) * len(nums) // 2 - sum(nums)
```

### Next Permutation

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] >= nums[i + 1]:
                i -= 1
            else:
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i + 1:] = nums[i + 1:][::-1]
                        return
        nums.reverse()
```

### Number of Islands

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = '0'
            q = [(i, j)]
            while q:
                x, y = q.pop()
                if x > 0 and grid[x - 1][y] == '1':
                    grid[x - 1][y] = '0'
                    q.append((x - 1, y))
                if y > 0 and grid[x][y - 1] == '1':
                    grid[x][y - 1] = '0'
                    q.append((x, y - 1))
                if x < m - 1 and grid[x + 1][y] == '1':
                    grid[x + 1][y] = '0'
                    q.append((x + 1, y))
                if y < n - 1 and grid[x][y + 1] == '1':
                    grid[x][y + 1] = '0'
                    q.append((x, y + 1))
                
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res
```

### Product of Array Except Self

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        # l -> r
        for i in range(1, l):
            res[i] = res[i - 1] * nums[i - 1]
        # r -> l
        productR = 1
        for i in range(l-1, -1, -1):
            res[i] *= productR
            productR *= nums[i]
        return res
```

### Range Sum of BST

```python
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(root):
            if root:
                if low <= root.val <= high:
                    self.res += root.val
                if low < root.val:
                    dfs(root.left)
                if high > root.val:
                    dfs(root.right)
        self.res = 0
        dfs(root)
        return self.res
```

### Reverse Nodes in k-Group

```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head: ListNode, tail: ListNode):
            prev = tail.next
            p = head
            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex
            return tail, head
    
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nex = tail.next
            head, tail = reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return dummy.next
```

### Shortest Distance from All Buildings

```python
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def BFS(start_x, start_y):
            visited = [[False] * N for k in range(M)]
            visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings
        
        if not grid or not grid[0]: 
            return -1
        M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
        hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]
    
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x, y): return -1
        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])
```

### Simplify Path

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for it in path.rstrip('/').split('/'):
            if it == '.' or it == "":
                continue
            elif it == "..":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(it)
        return '/' + '/'.join(res)
```

### Strobogrammatic Number

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6', '2':'#', '3':'#', '4':'#', '5':'#', '7':'#'}
        l = len(num)
        for i in range(l / 2 + 1):
            if dic[num[i]] != num[l - i - 1]:
                return False
        return True
```

### Strobogrammatic Number II

```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        n1 = ['0', '1', '8']
        n2 = ['11', '88', '69', '96', '00']
        if n == 1:
            return n1
        if n == 2:
            return n2[:-1]
        mid = (n - 1) / 2
        if n % 2 == 0:
            return [p[:mid] + c + p[mid:] for c in n2 for p in self.findStrobogrammatic(n - 2)]
        else:
            return [p[:mid] + c + p[mid:] for c in n1 for p in self.findStrobogrammatic(n - 1)]
```

### Subarray Sum Equals K

```python
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        s = 0
        dic[0] = 1
        res = 0
        for n in nums:
            s += n
            if s - k in dic:
                res += dic[s - k]
            dic[s] += 1
        return res
```

### Task Scheduler

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)
        maxx = max(ct.values())
        nmax = len([v for v in ct.values() if v == maxx])
        return max(len(tasks), (maxx - 1) * (n + 1) + nmax)
```

### Toeplitz Matrix

```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
```

### Valid Palindrome II

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
                return True
        i, j = 0, len(s)-1
        while i < j:
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                p = s[0: j] + s[j + 1: ]
                q = s[0: i] + s[i + 1: ]
                break
        if p == p[::-1] or q == q[::-1]:
            return True
        else:
            return False
```



### Verifying an Alien Dictionary

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if dic[word1[k]] > dic[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
```

### Word Break II

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(i):
            if i in memo:
                return memo[i]
            res = []
            for j in range(i, len(s)):
                prefix = s[i: j + 1]
                if prefix in wordDict:
                    tmp = dfs(j + 1)
                    for word in tmp:
                        res.append((prefix + " " + word).strip())
            memo[i] = res
            return res
        
        wordDict = set(wordDict)
        memo = {len(s): [""]}
        return dfs(0)
```

### Word Ladder

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        wordList.add(beginWord)
        l = len(beginWord)
        dic = defaultdict(list)
        for word in wordList:
            for i in range(l):
                tmp = word[:i] + '_' + word[i + 1:]
                dic[tmp].append(word)
        q1 = deque([beginWord])
        dis1 = {w: 0 for w in wordList}
        dis1[beginWord] = 1
        q2 = deque([endWord])
        dis2 = {w: 0 for w in wordList}
        dis2[endWord] = 1
        flag = True
        while q1 and q2:
            if flag:
                front, dis_front = q1, dis1
                back, dis_back = q2, dis2
            else:
                front, dis_front = q2, dis2
                back, dis_back = q1, dis1 
            cur = front.popleft()
            dist = dis_front[cur]
            next_word = []
            for i in range(l):
                tmp = cur[:i] + '_' + cur[i + 1:]
                for w in dic[tmp]:
                    next_word.append(w)
            for w in next_word:
                if dis_back[w] > 0:
                    return dist + dis_back[w]
                if dis_front[w] == 0:
                    dis_front[w] = dist + 1
                    front.append(w)
            if len(back) < len(front):
                flag = not flag
        return 0
```

### Walls and Gates

```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])
        q = []
        inf = 2147483647
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(q) > 0:
            i, j, d = q.pop(0)
            for dirx, diry in directions:
                tx, ty = i + dirx, j + diry
                if 0 <= tx < m and 0 <= ty < n:
                    if rooms[tx][ty] == inf:
                        rooms[tx][ty] = d + 1
                        q.append((tx, ty, d + 1))
```

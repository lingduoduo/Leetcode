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

### Construct Binary Tree from Preorder and Inorder Traversal

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def array_to_tree(left, right):
            if left > right: 
                return None
            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)
            self.preorder_index += 1
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)
            return root
        
        self.preorder_index = 0
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
        return array_to_tree(0, len(preorder) - 1)
```

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        s = []
        root = TreeNode(preorder[0])
        cur = root
        j = 0
        for i in range(1, len(preorder)):
            if cur.val != inorder[j]:
                cur.left = TreeNode(preorder[i])
                s.append(cur)
                cur = cur.left
            else:
                j += 1
                while s and s[-1].val == inorder[j]:
                    cur = s.pop()
                    j += 1
                cur.right = TreeNode(preorder[i])
                cur = cur.right
        return root
```

### Frog Jump

```python
class Solution:
    def canCross(self, stones: List[int]) -> bool:    
        @lru_cache(None)
        def dp(pos, k):
            if pos == stones[-1]: 
                return True
            if pos not in stoneset:
                return False
            return dp(pos + k + 1, k + 1) or dp(pos + k, k) or (dp(pos + k - 1, k - 1) if k > 1 else False)
        
        stoneset = set(stones)
        if len(stones) < 2: return False
        if stones[1] - stones[0] != 1: return False
        return dp(1, 1)
```

### Graph Valid Tree

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False
        dic = {}
        for i in range(n):
            dic[i] = []
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        visit = set([0])
        q = deque([0])
        while q:
            now = q.popleft()
            for v in dic[now]:
                if v not in visit:
                    q.append(v)
                    visit.add(v)
        return len(visit) == n

```

### House Robber II

```python
class Solution:
    def _rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for i in range(len(nums)):
            dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        return dp1
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))
```

### Insert Delete GetRandom O(1)

```python
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        last, idx = self.list[-1], self.dic[val]
        self.list[idx], self.dic[last] = last, idx
        del self.dic[val]
        del self.list[-1]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)
```

### Intersection of Two Linked Lists

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa
```

### Is Graph Bipartite?

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(v, c):
            color[v] = c
            for node in graph[v]:
                if color[node] == c:
                    return False
                if color[node] == 0 and not dfs(node, -c):
                    return False
            return True
        
        l = len(graph)
        color = [0] * l
        for i in range(l):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True
```

### Jump Game III

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        s = {start}
        q = [start]
        while q:
            cur = q.pop(0)
            for nei in (cur + arr[cur], cur - arr[cur]):
                if 0 <= nei < n:
                    if arr[nei] == 0:
                        return True
                    if nei not in s:
                        q.append(nei)
                        s.add(nei)
        return False
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

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            if not root:
                return
            res = inorder(root.left)
            if res is not None:
                return res
            self.k -= 1
            if self.k == 0:
                return root.val
            else:
                return inorder(root.right)
            
        self.k = k
        return inorder(root)
```

### Longest Valid Parentheses

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
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

### Number of Subsequences That Satisfy the Given Sum Condition

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod
```

### One Edit Distance

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls > lt:
            s, t = t, s
            ls, lt = lt, ls
        if ls == lt:
            tmp = 0
            for i in range(ls):
                if s[i] != t[i]:
                    tmp += 1
            return tmp == 1
        elif ls + 1 == lt:
            for i in range(ls):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True
        else:
            return False
```

### Permutations

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, i):
            if i == len(nums):
                res.append(nums[:])
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        res = []
        dfs(nums, 0)
        return res
```

### Permutations II

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            new_res = []
            for l in res:
                for i in range(len(l) + 1):
                    new_res.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break
            res = new_res
        return res
```

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(tmp, counter):
            if len(tmp) == len(nums):
                res.append(list(tmp))
                return

            for num in counter:
                if counter[num] > 0:
                    tmp.append(num)
                    counter[num] -= 1
                    dfs(tmp, counter)
                    tmp.pop()
                    counter[num] += 1
        dfs([], Counter(nums))
        return res
```

### Possible Bipartition

```python
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edge = [[] for _ in range(N + 1)]
        for u, v in dislikes:
            edge[u].append(v)
            edge[v].append(u)
        color = [0] * (N + 1)
        for i in range(1, N + 1):
            if color[i] == 0:
                q = [i]
                color[i] = 1
                while q:
                    cur = q.pop()
                    cur_c = color[cur]
                    for node in edge[cur]:
                        if color[node] == 0:
                            color[node] = cur_c * -1
                            q.append(node)
                        elif color[node] == cur_c:
                            return False
        return True
```

### Remove subdirectory

```python
def remove_subdirectory(paths):
    tire = {}
    for path in paths:
        cur = tire
        for item in path.split('/')[1:]:
            if '#' in cur:
                break
            if item not in cur:
                cur[item] = {}
            cur = cur[item]
        cur["#"] = {}
    res = []
    q = [(tire, [])]
    while q:
        cur, path = q.pop()
        if '#' in cur:
            res.append('/' + '/'.join(path))
            continue
        for ne in cur:
            q.append((cur[ne], path + [ne]))
    return res
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

### Search a 2D Matrix

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if matrix[0][0] > target or matrix[m - 1][n - 1] < target:
            return False
        tmp = []
        for i in range(m):
            tmp.append(matrix[i][0])
        ind = bisect.bisect_left(tmp, target)
        if ind == len(tmp):
            ind = ind - 1
        if target < matrix[ind][0]:
            ind = ind - 1
        ind2 = bisect.bisect_left(matrix[ind], target)
        if ind2 == n:
            return False
        return matrix[ind][ind2] == target
```

### Search a 2D Matrix II

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1
        return False
```

### Search in Rotated Sorted Array

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid] < target or \
                target < nums[l] <= nums[mid] or \
                nums[mid] < target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
```

### Serialize and Deserialize Binary Tree

```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        from collections import deque
        result = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            result.append(str(node.val) if node else 'None ')
            if node:
                q.append(node.left)
                q.append(node.right)
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        ls = data.split()
        root = TreeNode(ls[0])
        queue = collections.deque()
        queue.append(root)
        i = 1
        
        while queue and i < len(ls):
            node = queue.popleft()
            if ls[i] != 'None':
                left = TreeNode(ls[i])
                node.left = left
                queue.append(left)
            i += 1
            
            if ls[i] != 'None':
                right = TreeNode(ls[i])
                node.right = right
                queue.append(right)
            i += 1
        
        return root
```

### Sliding Window Maximum

```python
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = deque()
        for i in range(n):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
```

### Sort Colors

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1, p2 = 0, 0, len(nums) - 1
        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
            elif nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
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

### The Maze III

```python
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n, q, stopped = len(maze), len(maze[0]), [(0, "", ball[0], ball[1])], {(ball[0], ball[1]): [0, ""]}
        while q:
            dist, pattern, x, y = heapq.heappop(q)
            if [x, y] == hole:
                return pattern
            for i, j, p in ((-1, 0, "u"), (1, 0, "d"), (0, -1, "l"), (0, 1, "r")):
                newX, newY, d = x, y, 0
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                    d += 1
                    if [newX, newY] == hole:
                        break
                if (newX, newY) not in stopped or [dist + d, pattern + p] < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, newX, newY))
        return "impossible"
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

### Word Break

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                l = len(w)
                if s[i - l: i] == w and dp[i - l]:
                    dp[i] = True
                    break
        return dp[-1]
```

## 设计 facebook首页

## 设计credit card支付系统

## 设计reporting system

## 设计超小网站网址

## 设计类似脸书新闻馈送 后台，怎么支持已读功能（把已读的内容从推送中删除）

## news feed

## System Design：Design crawler

## System Design：Design calender


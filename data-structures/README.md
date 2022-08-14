#### 目录

1 Recursion / Backtracking [递归回溯法]

- [Combination-Sum](https://leetcode.com/problems/combination-sum/)
- [Combination-Sum II](https://leetcode.com/problems/combination-sum-ii/)
- [ Subsets](https://leetcode.com/problems/subsets/)
- [Subsets II](https://leetcode.com/problems/subsets-ii/)
- [Permutation](https://leetcode.com/problems/permutations/)
- [Permutation II](https://leetcode.com/problems/permutations-ii/)

2 Graph Traversal [图遍历]

- [Word Ladder](https://leetcode.com/problems/word-ladder/)
- [Clone Graph](https://leetcode.com/problems/clone-graph/)
- [The Maze] - Premium
- [Course Schedule](https://leetcode.com/problems/course-schedule/)
- [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [Alien Dictionary] - Premium

3 树

- [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)
- [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [Complete Binary Tree Inserter](https://leetcode.com/problems/complete-binary-tree-inserter/)

4 二分查找

- [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

5 Data Structure - HashTable, Stack, Priority Queue

- [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [Min Stack](https://leetcode.com/problems/min-stack/)
- [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

6 LinkList

7 Pointer Manipulation [查找子字符串，双指针模板]

8 排序的写法

9 Desgin

10 [动态规划](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_1263)

- [并查集](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_630)

- [前缀树](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_747)

- [状态搜索](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_1265)

- [贪心](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_1303)

### Recursion / Backtracking 回溯法

这个回溯思想，先去添加一个新的状态，看在这个状态的基础上，能不能找结果，如果找不到结果的话，那么就回退，即把这个结果和访问的记录给去掉。这个题使用了return True的方法让我们知道已经找出了结果，所以不用再递归了。

(39. Combination-Sum )

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res
    
    def dfs(self, candidates, target, idx, path):
        if target == 0:
            self.res.append(path)
            return
        
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]])
```

(40. Combination-Sum II)

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res
    
    def dfs(self, candidates, target, idx, path):
        if target == 0:
            self.res.append(path)
            return
        
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]])  
```

(78. Subsets)

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        for i in range(1 + len(nums)):
            self.dfs(nums, i, 0, [])
        return self.res

    def dfs(self, nums, n, idx, path):
        if n == len(path):
            self.res.append(path)
            return

        for i in range(idx, len(nums)):
            self.dfs(nums, n, i + 1, path + [nums[i]]) 
```

(90. Subsets II)

```python
class Solution:
    def subsetsWithDup(self, nums):
        self.res = []
        nums.sort()
        for i in range(len(nums)):
            self.dfs(nums, i, [])
        return self.res

    def dfs(self, nums, index, path):
        if path not in self.res:
            self.res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]])
```

(46. Permutation)

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        if len(nums) == 0:
            self.res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], [nums[i]] + path)
```

(47. Permutation II)

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        self.dfs(nums, [])
        return list(self.res)

    def dfs(self, nums, path):            
        if len(nums) == 0:
            self.res.add(tuple(path))
            return
        for i in range(len(nums)):                
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]])
```

### 图遍历

[127. Word Ladder]

```python
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        stack = [(beginWord, 1)]
        visited = set()
        wordList = set(wordList)

        while (stack):
            next_child = []
            for node, step in stack:
                if node == endWord:
                    return step
                if node not in visited:
                    visited.add(node)
                    for i in range(len(node)):
                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            if node[:i] + j + node[i + 1:] in wordList:
                                next_child.append((node[:i] + j + node[i + 1:], step + 1))
            stack = list(set(next_child))
        return 0
```

(133. Clone Graph)

```python
class Solution: 
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        d = dict()
        d[node] = Node(node.val, [])
        stack = collections.deque()
        stack.append(node)
        
        while stack:
            cur = stack.popleft()
            if not cur:
                continue
            for neighbor in cur.neighbors:
                if neighbor not in d:
                    d[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                d[cur].neighbors.append(d[neighbor])
        return d[node]
```

(490. The Maze)

```python
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    		m, n = len(maze), len(maze[0])
        visit = set()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        stack = [start]
        while stack:
            curx, cury = stack.pop()
            if [curx, cury] == destination:
                return True
            for dirx, diry in directions:
                tx, ty = curx, cury
                while 0 <= tx + dirx < m and 0 <= ty + diry < n and not maze[tx + dirx][ty + diry]:
                    tx, ty = tx + dirx, ty + diry
                if (tx, ty) not in visit:
                    visit.add((tx, ty))
                    stack.append((tx, ty))
        return False
```

[207. Course Schedule]

BFS方式：
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inbound = [0] * numCourses
        edge = defaultdict(list)
        for x, y in prerequisites:
            inbound[x] += 1
            edge[y].append(x)
        stack = [i for i in range(numCourses) if inbound[i] == 0]
        visited = 0
        while stack:
            cur = stack.pop()
            visited += 1
            for node in edge[cur]:
                inbound[node] -= 1
                if inbound[node] == 0:
                    stack.append(node)
        return visited == numCourses
```

DFS方式：

```python
class Solution(object):
    def canFinish(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        ###0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * N
        for i in range(N):
            if not self.dfs(graph, visited, i):
                return False
        return True

    ###Can we add node i to visited successfully?
    def dfs(self, graph, visited, i):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True
```

如果需要保存拓扑排序的路径：

[210. Course Schedule II]

BFS方式：

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        edge = defaultdict(list)
        for x, y in prerequisites:
            indegree[x] += 1
            edge[y].append(x)
        q = [i for i in range(numCourses) if indegree[i] == 0]
        res = []
        while q:
            cur = q.pop()
            res.append(cur)
            for n in edge[cur]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        return res if len(res) == numCourses else []
```

DFS方式：

```python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        ###0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path):
                return []
        return path

    def dfs(self, graph, visited, i, path):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, path):
                return False
        visited[i] = 2
        path.append(i)
        return True
```

[269. Alien Dictionary]

```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create adject matrx of the graph
        adj_list = collections.defaultdict(set)
        # create initial indegrees 0 for all distinct words
        indegrees = {}
        for word in words:
            for c in word:
                if c in indegrees:
                    continue
                indegrees[c] = 0

        # construct the graph and indegrees
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    # this line is needed, otherwise the indegrees of d will be repeatedly added
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegrees[d] += 1
                    break
            # this 'else' will still match with the 'if' inside the for loop, it means if after any zip pairs c and d is not equal, codes in 'else' won't be runned. only when all pairs are equal, then codes in 'else' will be runned. In other words, the 'else' match to the final 'if' of the for loop
            else:
                # check if the second word is a prefix of the first word
                if len(second_word) < len(first_word):
                    return ''

        # pick all nodes with zero indegree and put it into queue
        q = collections.deque()
        for k, v in indegrees.items():
            if v == 0:
                q.append(k)

        # pick off zero indegree nodes level by level,and add to the output
        ans = []
        while q:
            c = q.popleft()
            ans.append(c)
            for d in adj_list[c]:
                indegrees[d] -= 1
                if indegrees[d] == 0:
                    q.append(d)

        # if there are letter that not appear in the output, means there is a cycle in the graph, because on the indegrees of nodes in a cycle will all be non-zero
        if len(ans) < len(indegrees):
            return ''

        return "".join(ans)
```

### 树

前序遍历

[144. Binary Tree Preorder Traversal]

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
```

中序遍历

[94. Binary Tree Inorder Traversal]

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res
```

后序遍历

[145. Binary Tree Postorder Traversal]

迭代写法如下：

```python
        stack, res = [root], deque([])
        while stack:
            cur = stack.pop()
            if cur:
                res.appendleft(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
        return res
```

[102. Binary Tree Level Order Traversal]
```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            nodes = []
            for i in range(len(stack)):
                node = stack.pop(0)
                nodes.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(nodes)
        return res
```

[236.  Lowest Common Ancestor of a Binary Tree]

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q==root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```

(297. Serialize and Deserialize Binary Tree)

```python
class Codec:

    def serialize(self, root):
        self.res = []
        self.preorder(root)
        return ','.join(str(s) for s in self.res)

    def preorder(self, root):
        if root is None:
            self.res.append("#")
            return
        self.res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        return

    def deserialize(self, data):
        vals = collections.deque(val for val in data.split(','))
        return self.build(vals)

    def build(self, vals):
        if not vals:
            return None

        val = vals.popleft()
        if val == '#':
            return None
        root = TreeNode(int(val))
        root.left = self.build(vals)
        root.right = self.build(vals)
        return root
```

[617. Merge Two Binary Trees]

把两个树重叠，重叠部分求和，不重叠部分是两个树不空的节点。

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root2:
            return root1
        if not root1:
            return root2
        newT = TreeNode(root1.val + root2.val)
        newT.left = self.mergeTrees(root1.left, root2.left)
        newT.right = self.mergeTrees(root1.right, root2.right)
        return newT
```

Binary Search Tree

[98.Validate Binary Search Tree)

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.valid(root, float("-inf"), float("inf"))
    
    def valid(self, root, left, right):
        if not root:
            return True
        
        if root.val <= left or root.val >= right:
            return False
        
        return self.valid(root.left, left, root.val) and self.valid(root.right, root.val, right)
```

构建完全二叉树

完全二叉树是每一层都满的，因此找出要插入节点的父亲节点是很简单的。如果用数组tree保存着所有节点的层次遍历，那么新节点的父亲节点就是tree[(N -1)/2]，N是未插入该节点前的树的元素个数。
构建树的时候使用层次遍历，也就是BFS把所有的节点放入到tree里。插入的时候直接计算出新节点的父亲节点。获取root就是数组中的第0个节点。

[919. Complete Binary Tree Inserter]

```python
class CBTInserter:

    def __init__(self, root):
        self.tree = list()
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            self.tree.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v):
        _len = len(self.tree)
        father = self.tree[(_len - 1) // 2]
        node = TreeNode(v)
        if not father.left:
            father.left = node
        else:
            father.right = node
        self.tree.append(node)
        return father.val

    def get_root(self):
        return self.tree[0]
```

### 二分查找

其中f(m)函数代表找到了满足条件的情况，有这个条件的判断就返回对应的位置，如果没有这个条件的判断就是lowwer_bound和higher_bound.

```python
def binary_search(l, r):
    while l < r:
        m = l + (r - l) // 2
        if f(m):  ###判断找了没有，optional
            return m
        if g(m):
            r = m  ###new range [l, m)
        else:
            l = m + 1  ###new range [m+1, r)
    return l  ###or not found
```

[34. Find First and Last Position of Element in Sorted Array]

区间定义：`[l, r) 左闭右开`

**lower bound**: find index of i, such that `A[i] >= x`

**upper bound**: find index of i, such that `A[i] > x`

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lower_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
    
    def lower_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def higher_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left
```

[69. Sqrt(x)]

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 0, x//2 + 1
        ###[left, right)
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1
```

(162. Find Peak Element )

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                left = mid2
            else:
                right = mid1
        return left
```
### Data Structure - HashTable, Queue, Priority Queue

HashTable

[242. Valid Anagram]

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for cha in s:
            if cha in d:
                d[cha] += 1
            else:
                d[cha] = 1

        for cha in t:
            if cha in d:
                if d[cha] > 0:
                    d[cha] -= 1
                else:
                    return False
            else:
                return False
        return all(v == 0 for v in d.values())
```

Stack

[155. Min Stack]

```python
class MinStack:

    def __init__(self):
        self.num_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.num_stack.append(val)
        if len(self.min_stack) == 0 or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.min_stack.pop()
        return None if len(self.num_stack) == 0 else self.num_stack.pop()

    def top(self) -> int:
        return None if len(self.num_stack) == 0 else self.num_stack[-1]

    def getMin(self) -> int:
        return None if len(self.min_stack) == 0 else self.min_stack[-1]
```

(225. Implement Stack using Queues)

```python
class MyStack:
    def __init__(self):
        self.que = collections.deque()

    def push(self, x):
        self.que.append(x)
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

    def pop(self):
        return self.que.popleft()

    def top(self):
        return self.que[0]

    def empty(self):
        return not self.que
```

Priority Queue

[23. Merge k Sorted Lists]

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next
        
        dummy = ListNode()
        cur = dummy
        while q:
            val, i = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i))
                lists[i] = lists[i].next
        return dummy.next
```

[215. Kth Largest Element in an Array)

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        i = 0
        while i < k:
            res = heapq.heappop(nums)
            i += 1
        return -res
```

### Linklist

(237. Delete Node in a Linked List)

```python
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```

(876. Middle of the Linked List)

```
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
```

(92. Reverse Linked List II)

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        root = ListNode(0)
        root.next = head
        pre = root
        while pre.next and count < left:
            pre = pre.next
            count += 1
        if count < left:
            return head
        mNode = pre.next
        curr = mNode.next
        while curr and count < right:
            next = curr.next
            curr.next = pre.next
            pre.next = curr
            mNode.next = next
            curr = next
            count += 1
        return root.next
```

(143. Reorder List)

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            
            #find mid
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head1 = head
            head2 = slow.next
            slow.next = None
            
            # reverse second list
            dummy = ListNode(0)
            dummy.next = head2
            curr = head2.next
            head2.next = None
            
            while curr:
                dummy.next, curr.next, curr = curr, dummy.next, curr.next
            head2 = dummy.next
        
            # merge two linked list head1 and head2
            p1 = head1
            p2 = head2
            while p2:
                p1.next, p2.next, p1, p2 = p2, p1.next, p1.next, p2.next 
```

### Pointer Manipulation

(3. Longest Substring Without Repeating Characters)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = res = 0
        for i, c in enumerate(s):
            if c in d and start <= d[c]:
                start = d[c] + 1
            else:
                res = max(res, i - start + 1)
            d[c] = i
        return res
```

[76. Minimum Window Substring]

这个题的map是t的字频，所以使用map更方式和上是相反的。

```python
class Solution(object):
    def minWindow(self, s, t):
        res = ""
        left, cnt, minLen = 0, 0, float('inf')
        count = collections.Counter(t)
        for i, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                cnt += 1
            while cnt == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left: i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    cnt -= 1
                left += 1
        return res
```

(239. Sliding Window Maximum)
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

### 排序的写法

[451. Sort Characters By Frequency]

```python
class Solution(object):
    def frequencySort(self, s):
        import collections

        i = [cha for cha in s]
        d = collections.Counter(i)
        f = d.most_common()
        return ''.join([k * v for k, v in f])
```

(148. Sort List)

```python
class Solution:
    def merge(self, h1, h2):
        dummy = tail = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
```

Design

(146. LRU Cache)

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

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.capacity = capacity
        self.size = 0
        self.root = ListNode(0, 0)

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value
        else:
            if self.size >= self.capacity:
                self.removeFromTail()
                self.size -= 1
            node = ListNode(key, value)
            self.insertIntoHead(node)
            self.dic[key] = node
            self.size += 1

    def removeFromList(self, node):
        if node == self.root: return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None

    def insertIntoHead(self, node):
        head_node = self.root.next
        head_node.prev = node
        node.prev = self.root
        self.root.next = node
        node.next = head_node

    def removeFromTail(self):
        if self.size == 0: return
        tail_node = self.root.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)
```

(1066. )

```
class Solution:
    def assignBikes(self, workers, bikes):
        n, m = len(workers), len(bikes)
        dis = [[0 for _ in range(m)] for _ in range(n)]
            
        for w, worker in enumerate(workers):
             xw, yw = worker[0], worker[1]
            
             for b, bike in enumerate(bikes):
                xb, yb = bike[0], bike[1]
                dis[w][b] = abs(xb-xw) + abs(yb-yw)

        def findRes(wid, usedbike):
            if wid >= n:
                return 0 
            
            state = (wid, tuple(sorted(list(usedbike))))
            # print state
            if state in dp: #Calculated before
                return dp[state]
            else:
                res = float("inf")
                for bid in range(m):
                    if bid not in usedbike:    
                        usedbike.add(bid)
                        t = dis[wid][bid] + findRes(wid + 1, usedbike)   
                        usedbike.remove(bid)
                        res = min(res, t)
                dp[state] = res
                return res
```

### 并查集

不包含rank的话，代码很简短，应该背会。

(721. Accounts Merge)

```python
class DSU:
    def __init__(self):
        self.par = range(10001)

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

    def same(self, x, y):
        return self.find(x) == self.find(y)
```

包含rank的，这里的rank表示树的高度：

[684. Redundant Connection]

```python
class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True
```

另外一种rank方法是，保存树中节点的个数。

[547. Friend Circles]

```python
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        dsu = DSU()
        N = len(M)
        for i in range(N):
            for j in range(i, N):
                if M[i][j]:
                    dsu.u(i, j)
        res = 0
        for i in range(N):
            if dsu.f(i) == i:
                res += 1
        return res

class DSU(object):
    def __init__(self):
        self.d = range(201)
        self.r = [0] * 201

    def f(self, a):
        return a if a == self.d[a] else self.f(self.d[a])

    def u(self, a, b):
        pa = self.f(a)
        pb = self.f(b)
        if (pa == pb):
            return
        if self.r[pa] < self.r[pb]:
            self.d[pa] = pb
            self.r[pb] += self.r[pa]
        else:
            self.d[pb] = pa
            self.r[pa] += self.r[pb]
```

### 前缀树

前缀树的题目可以使用字典解决，代码还是需要背一下的，C++版本的前缀树如下：

[208. Implement Trie (Prefix Tree)]

```python
class Trie:
    def __init__(self):
        """ Initialize your data structure here. """
        self.dic = {}

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie. """
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True
        print(self.dic)

    def search(self, word: str) -> bool:
        """ Returns if the word is in the trie. """
        cur = self.dic
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        """ Returns if there is any word in the trie that starts with the given prefix. """
        cur = self.dic
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    obj.search("apple")
    obj.insert("apps")
    obj.startsWith("app")
    obj.insert("app")
    obj.startsWith("app")
```

[677. Map Sum Pairs]

#### 查找子字符串，双指针模板

这是一个[模板](https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'
rel=)，里面的map如果是双指针范围内的字符串字频的话，增加和减少的方式如下。


```

### 动态规划

[312. Burst Balloons]

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]
```

#### 状态搜索

[688. Knight Probability in Chessboard]

[62. Unique Paths]

[63. Unique Paths II]

[913. Cat and Mouse]

[576. Out of Boundary Paths]

```python
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        for s in range(1, N + 1):
            curStatus = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    v1 = 1 if x == 0 else dp[x - 1][y]
                    v2 = 1 if x == m - 1 else dp[x + 1][y]
                    v3 = 1 if y == 0 else dp[x][y - 1]
                    v4 = 1 if y == n - 1 else dp[x][y + 1]
                    curStatus[x][y] = (v1 + v2 + v3 + v4) % (10 ** 9 + 7)
            dp = curStatus
        return dp[i][j]
```

### 贪心

贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来最好的选择。也就是说，不从整体最优上加以考虑，他所作出的是在某种意义上的局部最优解。贪心算法和动态规划算法都是由局部最优导出全局最优，这里不得不比较下二者的区别

贪心算法： 
1.贪心算法中，作出的每步贪心决策都无法改变，因为贪心策略是由上一步的最优解推导下一步的最优解，而上一部之前的最优解则不作保留。 
2.由（1）中的介绍，可以知道贪心法正确的条件是：每一步的最优解一定包含上一步的最优解

动态规划算法： 
1.全局最优解中一定包含某个局部最优解，但不一定包含前一个局部最优解，因此需要记录之前的所有最优解 
2.动态规划的关键是状态转移方程，即如何由以求出的局部最优解来推导全局最优解
3.边界条件：即最简单的，可以直接得出的局部最优解

贪心是个思想，没有统一的模板。


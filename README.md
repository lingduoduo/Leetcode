test

#### 目录

- [二分查找](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_6)

- [排序的写法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_84)

- [BFS的写法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#BFS_104)

- [DFS的写法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#DFS_248)

- [回溯法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_288)

- [树](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_415)

-
    - [递归](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_417)
    - [迭代](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_435)
    - [前序遍历](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_465)
    - [中序遍历](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_500)
    - [后序遍历](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_533)

- [构建完全二叉树](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_569)

- [并查集](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_630)

- [前缀树](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_747)

- [图遍历](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_869)

-
    - [Dijkstra算法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#Dijkstra_873)
    - [Floyd-Warshall算法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#FloydWarshall_902)
    - [Bellman-Ford算法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#BellmanFord_928)

- [最小生成树](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_952)

-
    - [Kruskal算法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#Kruskal_956)
    - [Prim算法](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#Prim_1006)

- [拓扑排序](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_1065)

- [查找子字符串，双指针模板](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_1201)

- [动态规划](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_1263)

-
    - [状态搜索](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_1265)

- [贪心](https://blog.csdn.net/fuxuemingzhu/article/details/101900729#_1303)

本文的目的是收集一些典型的题目，记住其写法，理解其思想，即可做到一通百通。欢迎大家提出宝贵意见！

#### 二分查找

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

```python
def lowwer_bound(self, nums, target):
    ###find in range [left, right)
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

**upper bound**: find index of i, such that `A[i] > x`

```python
def higher_bound(self, nums, target):
    ###find in range [left, right)
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
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1
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

#### 排序的写法

[451. Sort Characters By Frequency]

```python
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = dict()

        res = ''
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

        for key in sorted(d, key=d.get, reverse=True):
            res += ''.join([key] * d[key])
        return res


class Solution(object):
    def frequencySort(self, s):
        import collections

        i = [cha for cha in s]
        d = collections.Counter(i)
        f = d.most_common()
        return ''.join([k * v for k, v in f])


if __name__ == '__main__':
    s = "tree"
    s = "cccaaa"
    s = "Aabb"
    result = Solution().frequencySort(s)
    print(result)
```

#### BFS的写法

[863. All Nodes Distance K in Binary Tree]

下面的这个写法是在一个邻接矩阵中找出离某一个点距离是k的点

```python
###BFS

class Solution(object):
    def distanceK(self, root, target, K):
        bfs = [target.val]
        visited = set([target.val])
        for k in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in visited]
            visited |= set(bfs)
        return bfs

if __name__ == '__main__':
    p = TreeNode(3)
    p.left = TreeNode(5)
    p.right = TreeNode(1)
    p.left.left = TreeNode(6)
    p.left.right = TreeNode(2)
    p.left.right.left = TreeNode(7)
    p.left.right.right = TreeNode(4)
    p.right.right = TreeNode(8)

    result = Solution().distanceK(p, p.left, 2)
    print(result)
```

[127. Word Ladder]

在BFS中保存已走过的步，并把已经走的合法路径删除掉。

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

[Leetcode 778. Swim in Rising Water]

使用优先级队列来优先走比较矮的路，最后保存最高的那个格子的高度。

```python
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited, pq = set((0, 0)), [(grid[0][0], 0, 0)]
        res = 0
        while pq:
            T, i, j = heapq.heappop(pq)
            res = max(res, T)
            directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            if i == j == n - 1:
                break
            for dir in directions:
                x, y = i + dir[0], j + dir[1]
                if x < 0 or x >= n or y < 0 or y >= n or (x, y) in visited:
                    continue
                heapq.heappush(pq, (grid[x][y], x, y))
                visited.add((x, y))
        return res
```

[Leetcode 847. Shortest Path Visiting All Nodes]

需要找出某顶点到其他顶点的最短路径。出发顶点不是确定的，每个顶点有可能访问多次。使用N位bit代表访问过的顶点的状态。如果到达了最终状态，那么现在步数就是所求。这个题把所有的节点都放入了起始队列中，相当于每次都是所有的顶点向前走一步。

```python
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        que = collections.deque()
        step = 0
        goal = (1 << N) - 1
        visited = [[0 for j in range(1 << N)] for i in range(N)]
        for i in range(N):
            que.append((i, 1 << i))
        while que:
            s = len(que)
            for i in range(s):
                node, state = que.popleft()
                if state == goal:
                    return step
                if visited[node][state]:
                    continue
                visited[node][state] = 1
                for nextNode in graph[node]:
                    que.append((nextNode, state | (1 << nextNode)))
            step += 1
        return step
```

[429. N-ary Tree Level Order Traversal]

多叉树的层次遍历，这个BFS写法我觉得很经典。适合记忆。

```python
"""
###Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        que = collections.deque()
        que.append(root)
        while que:
            level = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                level.append(node.val)
                for child in node.children:
                    que.append(child)
            if level:
                res.append(level)
        return res
```

#### DFS的写法

[329. Longest Increasing Path in a Matrix]

[417. Pacific Atlantic Water Flow]

[778. Swim in Rising Water]

二分查找+DFS

```python
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        left, right = 0, n * n - 1
        while left <= right:
            mid = left + (right - left) / 2
            if self.dfs([[False] * n for _ in range(n)], grid, mid, n, 0, 0):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def dfs(self, visited, grid, mid, n, i, j):
        visited[i][j] = True
        if i == n - 1 and j == n - 1:
            return True
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dir in directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or max(mid, grid[i][j]) != max(mid, grid[x][y]):
                continue
            if self.dfs(visited, grid, mid, n, x, y):
                return True
        return False
```

#### 回溯法

下面这个题使用了回溯法，但是写的不够简单干练，遇到更好的解法的时候，要把这个题进行更新。

这个回溯思想，先去添加一个新的状态，看在这个状态的基础上，能不能找结果，如果找不到结果的话，那么就回退，即把这个结果和访问的记录给去掉。这个题使用了return True的方法让我们知道已经找出了结果，所以不用再递归了。

[753. Cracking the Safe] 

```python
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ["0"] * n
        size = k ** n
        visited = set()
        visited.add("".join(res))
        if self.dfs(res, visited, size, n, k):
            return "".join(res)
        return ""

    def dfs(self, res, visited, size, n, k):
        if len(visited) == size:
            return True
        node = "".join(res[len(res) - n + 1:])
        for i in range(k):
            node = node + str(i)
            if node not in visited:
                res.append(str(i))
                visited.add(node)
                if self.dfs(res, visited, size, n, k):
                    return True
                res.pop()
                visited.remove(node)
            node = node[:-1]
```

[312. Burst Balloons]

```python
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        c = [[0] * (n + 2) for _ in range(n + 2)]
        return self.dfs(nums, c, 1, n)

    def dfs(self, nums, c, i, j):
        if i > j: return 0
        if c[i][j] > 0: return c[i][j]
        if i == j: return nums[i - 1] * nums[i] * nums[i + 1]
        res = 0
        for k in range(i, j + 1):
            res = max(res,
                      self.dfs(nums, c, i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] + self.dfs(nums, c, k + 1, j))
        c[i][j] = res
        return c[i][j]
```

#### 树

#### 递归

[617. Merge Two Binary Trees]

把两个树重叠，重叠部分求和，不重叠部分是两个树不空的节点。

```python
class Solution:
    def mergeTrees(self, t1, t2):
        if not t2:
            return t1
        if not t1:
            return t2
        newT = TreeNode(t1.val + t2.val)
        newT.left = self.mergeTrees(t1.left, t2.left)
        newT.right = self.mergeTrees(t1.right, t2.right)
        return newT
```

#### 迭代

[226. Invert Binary Tree]

```python
Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root
```

#### 前序遍历

[144. Binary Tree Preorder Traversal]

迭代写法：

```python
###Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res
```

#### 中序遍历

[94. Binary Tree Inorder Traversal]

迭代写法：

```python
# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        answer = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return answer
            root = stack.pop()
            answer.append(root.val)
            root = root.right
```

#### 后序遍历

[145. Binary Tree Postorder Traversal]

迭代写法如下：

```python
###Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

####recursive
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        res = list()
        
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res

####reverse post-order
class Solution(object):
    def postorderTraversal(self, root):
        if not root: return []
        
        res = []
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
```

#### 构建完全二叉树

完全二叉树是每一层都满的，因此找出要插入节点的父亲节点是很简单的。如果用数组tree保存着所有节点的层次遍历，那么新节点的父亲节点就是tree[(N -1)/2]，N是未插入该节点前的树的元素个数。
构建树的时候使用层次遍历，也就是BFS把所有的节点放入到tree里。插入的时候直接计算出新节点的父亲节点。获取root就是数组中的第0个节点。

[919. Complete Binary Tree Inserter]

```python
###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
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
        """
        :type v: int
        :rtype: int
        """
        _len = len(self.tree)
        father = self.tree[(_len - 1) / 2]
        node = TreeNode(v)
        if not father.left:
            father.left = node
        else:
            father.right = node
        self.tree.append(node)
        return father.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.tree[0]

###Your CBTInserter object will be instantiated and called as such:
###obj = CBTInserter(root)
###param_1 = obj.insert(v)
###param_2 = obj.get_root()
```

#### 并查集

不包含rank的话，代码很简短，应该背会。

1. Accounts Merge
   https://leetcode.com/articles/accounts-merge/

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

#### 前缀树

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


#### 图遍历

[743. Network Delay Time](https://blog.csdn.net/fuxuemingzhu/article/details/82862769)这个题很详细。

#### Dijkstra算法

时间复杂度是O(N ^ 2 + E)，空间复杂度是O(N+E).

```python
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        K -= 1
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))
        dist = [float('inf')] * N
        dist[K] = 0
        done = set()
        for _ in range(N):
            smallest = min((d, i) for (i, d) in enumerate(dist) if i not in done)[1]
            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
            done.add(smallest)
        return -1 if float('inf') in dist else max(dist)
```

#### Floyd-Warshall算法

时间复杂度O(n^3)， 空间复杂度O(n^2)。

```python
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = [[float('inf')] * N for _ in range(N)]
        for time in times:
            u, v, w = time[0] - 1, time[1] - 1, time[2]
            d[u][v] = w
        for i in range(N):
            d[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return -1 if float('inf') in d[K - 1] else max(d[K - 1])
```

#### Bellman-Ford算法

时间复杂度O(ne)， 空间复杂度O(n)

```python
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dist = [float('inf')] * N
        dist[K - 1] = 0
        for i in range(N):
            for time in times:
                u = time[0] - 1
                v = time[1] - 1
                w = time[2]
                dist[v] = min(dist[v], dist[u] + w)
        return -1 if float('inf') in dist else max(dist)
```

#### 最小生成树

[1135. Connecting Cities With Minimum Cost]

#### Kruskal算法


#### Prim算法


#### 拓扑排序

BFS方式：

```python
class Solution(object):
    def canFinish(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree: return False
            indegrees[j] = -1
            for node in graph[j]:
                indegrees[node] -= 1
        return True                
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

BFS方式：

```python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        path = []
        for i in range(numCourses):
            zeroDegree = False
            for j in range(numCourses):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree:
                return []
            indegrees[j] -= 1
            path.append(j)
            for node in graph[j]:
                indegrees[node] -= 1
        return path
```

DFS方式：

```python
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
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

[207. Course Schedule](https://blog.csdn.net/fuxuemingzhu/article/details/82951771)

[210. Course Schedule II](https://blog.csdn.net/fuxuemingzhu/article/details/83302328)

[310. Minimum Height Trees](https://blog.csdn.net/fuxuemingzhu/article/details/83548874)

#### 查找子字符串，双指针模板

这是一个[模板](https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'
rel=)，里面的map如果是双指针范围内的字符串字频的话，增加和减少的方式如下。

[76. Minimum Window Substring]

这个题的map是t的字频，所以使用map更方式和上是相反的。

```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
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

#### 动态规划

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

#### 贪心

贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来最好的选择。也就是说，不从整体最优上加以考虑，他所作出的是在某种意义上的局部最优解。贪心算法和动态规划算法都是由局部最优导出全局最优，这里不得不比较下二者的区别

贪心算法： 
1.贪心算法中，作出的每步贪心决策都无法改变，因为贪心策略是由上一步的最优解推导下一步的最优解，而上一部之前的最优解则不作保留。 
2.由（1）中的介绍，可以知道贪心法正确的条件是：每一步的最优解一定包含上一步的最优解

动态规划算法： 
1.全局最优解中一定包含某个局部最优解，但不一定包含前一个局部最优解，因此需要记录之前的所有最优解 
2.动态规划的关键是状态转移方程，即如何由以求出的局部最优解来推导全局最优解
3.边界条件：即最简单的，可以直接得出的局部最优解

贪心是个思想，没有统一的模板。


### secret value 链表
follow up还问了一下怎么判断输入链表是valid的

```python
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedListSecret:
    def __init__(self, val):
        self.val = val
        self.secret = 0
        self.next = None
def secret_value(node, hash_func):
    s = []
    while node:
        s.append(LinkedListSecret(node.val))
        node = node.next
    nextt = s.pop()
    nextt.secret = hash_func(nextt.val)
    while s:
        cur = s.pop()
        cur.secret = hash_func(cur.val + nextt.secret)
        cur.next = nextt
        nextt = cur
    return nextt
def f(n):
    return n % 7
```

### 压缩有向图

```python
class Node:
    def __init__(self, val):
        self.s = val
        self.next = []
        self.in_degree = 0
        self.out_degree = 0

def compress(graph):
    def dfs(node):
        if node.out_degree == 1 and node.next[0].in_degree == 1:
            dfs_ret = dfs(node.next[0])
            node.s = node.s + dfs_ret.s
            node.next = dfs_ret.next
            node.out_degree = dfs_ret.out_degree
            dfs_ret.s = "#"
        else:
            for nextt in node.next:
                dfs(nextt)
        return node

    for node in graph:
        node.out_degree = len(node.next)
        for n in node.next:
            n.in_degree += 1

    for node in graph:
        if node.in_degree == 0:
            dfs(node)
```

### 距离1最远

一个0 1 矩阵，给起点和终点要求你找到从起点到终点的一条路，使得path里每个位置离1的位置尽量远
LC1102

```python

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        pq = [(-grid[0][0], 0, 0)]
        distance = defaultdict(lambda: -1)
        distance[(0, 0)] = grid[0][0]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set([(0, 0)])
        m = len(grid)
        n = len(grid[0])
        while pq:
            curw, curx, cury = heapq.heappop(pq)
            if curx == m - 1 and cury == n - 1:
                return -curw
            curw = -curw
            for dirx, diry in directions:
                tmpx, tmpy = curx + dirx, cury + diry
                if 0 <= tmpx < m and 0 <= tmpy < n and (tmpx, tmpy) not in visit:
                    tw = min(curw, grid[tmpx][tmpy])
                    if distance[(tmpx, tmpy)] < tw:
                        distance[(tmpx, tmpy)] = tw
                        visit.add((tmpx, tmpy))
                        heapq.heappush(pq, (-tw, tmpx, tmpy))
```

### 轮流铺路
一个二维0 1矩阵，上面有两个岛是分开的（岛用1表示，0表示水）。两个人轮流铺路（0变成1），如果某一次改变以后两个岛连起来了，那个人就赢了。addRoadfunction的input就是要铺路的位置，如果两个岛连起来了就返回true，otherwise 返回false。addRoadfunction会不停的被call直到返回true

```python
from collections import defaultdict
class Solution(object):
    def __init__(self, grid):
        self.islands = 2
        self.grid = grid
        self.parent = {(x, y): (x, y) for x, y in grid}
        self.rank = defaultdict(int)

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 != p2:
            self.islands -= 1
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            else:
                self.parent[p1] = p2
                if self.rank[p1] == self.rank[p2]:
                    self.rank[p2] += 1

    def build(self, x, y):
        self.islands += 1
        self.grid.add((x, y))
        self.parent[(x, y)] = (x, y)
        if (x - 1, y) in self.grid:
            self.union((x, y), (x - 1, y))
        if (x + 1, y) in self.grid:
            self.union((x, y), (x + 1, y))
        if (x, y - 1) in self.grid:
            self.union((x, y), (x, y - 1))
        if (x, y + 1) in self.grid:
            self.union((x, y), (x, y + 1))
        return self.islands == 1
```

### Optimal Account Balancing

```python
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def dfs(i):
            while i < len(debt) and debt[i] == 0:
                i += 1
            if i == len(debt):
                return 0
            ret = float('inf')
            prev = 0
            for j in range(i + 1, len(debt)):
                if debt[j] != prev and debt[i] * debt[j] < 0:
                    debt[j] += debt[i]
                    ret = min(ret, 1 + dfs(i + 1))
                    debt[j] -= debt[i]
                    prev = debt[j]
            return ret
        
        bal = defaultdict(int)
        for f, t, a in transactions:
            bal[f] -= a
            bal[t] += a
        debt = [v for v in bal.values() if v != 0]
        return dfs(0)
```

### 岔路口炸弹
每个格子代表一个岔路口，碰到炸弹就死了，问能不能安全地从左上角走到右下角，自己设计怎么表示题

### House Robber

followup 如果最多m个

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for i in range(0, len(nums)):
            dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        return dp1
```
### Car Fleet

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        last_t = res = 0
        cars = sorted(zip(position, speed), key = lambda x: -x[0])
        for p, s in cars:
            t = (target - p) / s
            if t > last_t:
                res += 1
                last_t = t
        return res
```

### Car Fleet II

单行道小汽车，assume infinite time，速度快的追上慢的然后stuck with慢的，问几个cluster；followup 给车间距和时间;followup: 车速可以<0，代表反方向开

```python
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        res = [None] * n
        s = []
        for i in range(n - 1, -1, -1):
            while s:
                if cars[i][1] <= cars[s[-1]][1]:
                    s.pop()
                else:
                    if res[s[-1]] < 0:
                        break
                    d = res[s[-1]] * (cars[i][1] - cars[s[-1]][1])
                    if d >= cars[s[-1]][0] - cars[i][0]:
                        break
                    else:
                        s.pop()
            if not s:
                res[i] = -1
            else:
                res[i] = (cars[s[-1]][0] - cars[i][0]) /  (cars[i][1] - cars[s[-1]][1])
            s.append(i)
        return res
```

### Max Area of Island

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i - 1, j)
            return 0
        
        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0
```

### 用钻石造建筑

dfs出所有总value>target的解，然后贪心求最少的天数

### Vector 树
用vector 装所有的结点，但是每个节点里存的是父结点的下标而不是子节点。题目是给一个结点，删除它和它的子树。

遍历所有节点向上，遇到目标节点/删除的节点，把路径上的点删除，走到根，路径上所有节点标注，遇到不被删的节点标注成不被删

### log truncate

二分找到最多留多少log

```python
def log_truncate(ct, k):
    l, r = 0, max(ct.values())
    res = 0
    while l <= r:
        m = (l + r) // 2
        cur = sum(min(n, m) for n in ct.values())
        if cur == k:
            return m
        if cur < k:
            res = max(res, m)
            l = m + 1
        else:
            r = m - 1
    return l - 1
```

### 经典2D grid 走迷宫
和一个follow up， 非常直接。 讨论到了dp， bfs， dijkstra, binary search. 注意和面试官沟通，不要自己把问题弄麻烦。

### Find And Replace in String

```python
def findReplaceString(self, S, indexes, sources, targets):
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
        return S
```

### 砖头砌墙
有一堆砖头砌墙，每个砖头宽度不同，数量不限， 砌一层宽度为W的有多少种方法。 比如：砖头:A, BB, CCC, 宽度为6， 一种方法就可以是 ABBCCC。follow up砌h层有多少种方法，并且要保持稳定 == 相邻层不同砖之间的间隙不能在同一位置，

一层的情况类似coinchange，多层递归出所有解，然后比较任何两个解是否能相邻，因为每一层只与上一层有关，dp

### Basic Calculator III

```python
class Solution:
    def calculate(self, s: str) -> int:
        def operation(op, second, first):
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return first * second
            elif op == "/":
                tmp = first / second
                return int(first / second + .5) if tmp < 0 else int(tmp)
        def precedence(current_op, op_from_ops):
            if op_from_ops == "(" or op_from_ops == ")":
                return False
            if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
                return False
            return True
          
        if not s:
            return 0
        nums, ops = [], []
        i = 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            if c.isdigit():
                num = int(c)
                while i < len(s) - 1 and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                nums.append(num)
            elif c == "(":
                ops.append(c)
            elif c == ")":
                while ops[-1] != "(":
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
            elif c in ["+", "-", "*", "/"]:
                while len(ops) != 0 and precedence(c, ops[-1]):
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.append(c)
            i += 1
        while len(ops) > 0:
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
        return nums.pop()
```

### 最晚什么时候来等车

```python
def latest_time(shuttle, cap, people):
    tmp = []
    for s, c in zip(shuttle, cap):
        if c == 0:
            continue
        h, m = map(int, s.split(":"))
        tmp.append((h * 60 + m, c))
    for s in people:
        h, m = map(int, s.split(":"))
        tmp.append((h * 60 + m, -1))
    tmp.sort()
    p = 0
    dq = deque()
    last = 0
    flag = False
    lastshuttle = 0
    for i, item in enumerate(tmp):
        if item[1] == 0:
            continue
        if item[1] < 0:
            dq.append(item[0])
            continue
        if item[1] > 0:
            lastshuttle = item[0]
            if len(dq) >= item[1]:
                for _ in range(item[1]):
                    last = dq.popleft()
            else:
                last = dq[-1]
                dq.clear()
                flag = True
    res = lastshuttle if flag else last - 1
    return "%d:%02d" % (divmod(res, 60))
```

### Guess the Word 猜颜色

```python
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for i in range(10):
            guess = random.choice(wordlist)
            x = master.guess(guess)
            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(guess, w)) == x]
```

### query区间最大/小数

n个数，每次query一个区间，问最大的数 follow up O(n)空间

```python
class QueryMinMax:
    def __init__(self, arr):
        n = len(arr)
        tem = math.ceil(math.log2(n))
        self.arr = arr
        self.minn = [[0] * tem for _ in range(n)]
        self.maxn = [[0] * tem for _ in range(n)]
        for i in range(n):
            self.minn[i][0] = arr[i]
            self.maxn[i][0] = arr[i]
        for j in range(1, tem):
            for i in range(n - (1 << j) + 1):
                self.maxn[i][j] = max(self.maxn[i][j - 1], self.maxn[i + (1 << (j - 1))][j - 1])
                self.minn[i][j] = min(self.minn[i][j - 1], self.minn[i + (1 << (j - 1))][j - 1])

    def query_max(self, i, j):
        k = int(math.log2(j - i + 1))
        return max(self.maxn[i][k], self.maxn[j - (1 << k) + 1][k])

    def query_min(self, i, j):
        k = int(math.log2(j - i + 1))
        return minn(self.minn[i][k], self.minn[j - (1 << k) + 1][k])
```

### 汇报树

employee to ceo 每个employee有个vector存他的下属vector<Employee*> reports;给target，输出路径

### Coin Change

```python
# dp[i]表示组成i所需的最少硬币数
# dp[i] = min(dp[i], dp[i-coin] + 1) for c in coins if i >= coin
# dp[0] = 0
# dp[n]为所求
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```
### Minimum Number of Days to Eat N Oranges

给你一个整数，有三种操作：除二，除三，减一，问最少需要多少步能到达1

```python
class Solution:
    @lru_cache()
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n;
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3));   
```

### Majority Element

```python
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct = Counter(nums)
        l = len(nums) // 2
        for key, val in ct.items():
            if val > l:
                return key
```

### 岛中湖

计算一个二维数组(由L和W两种元素)中由Land跟被Land包围的W(Lake)所形成的continent的最大面积；follow up：计算将L元素变成W元素从而把所有Lake联通到Ocean(外部的W或者边界)的最小改变个数

从四周遍历，把外面标成2，再遍历整个矩阵，求每个岛的面经

followup，从2开始遍历，遇到湖之后，把全部湖加到front，继续遍历直到所有湖遍历完

### Matrix 惩罚

给一个matrix，每行选一个数，两个相邻行选的数的列号差为惩罚，求所选所有数的和减去惩罚的最大值

```python
def matrix(A):
    m, n = len(A), len(A[0])
    dp = [n for n in A[0]]
    for i in range(1, m):
        tmp = []
        for j in range(n):
            cur = 0
            for k in range(n):
                cur = max(cur, dp[k] - abs(j - k) + A[i][j])
            tmp.append(cur)
        dp = tmp
    return max(dp)
```

```python
def matrix(A):
    m, n = len(A), len(A[0])
    dp = [n for n in A[0]]
    for i in range(1, m):
        tmp = []
        l = [dp[0]]
        r = deque([dp[-1] - n + 1])
        for k in range(1, n):
            l.append(max(dp[k] + k, l[-1]))
        for k in range(n-2, -1, -1):
            r.appendleft(max(dp[k] - k, r[0]))
        for j in range(n):
            tmp.append(max(l[j] - j, r[j] + j) + A[i][j])
        dp = tmp
    return max(dp)
```

###  Kth Missing Positive Number

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
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
### Check if string follows order of characters defined by a pattern or not
https://www.geeksforgeeks.org/check-string-follows-order-characters-defined-pattern-not/

```python
def checkPattern(string, pattern):
    l = len(pattern)
    if len(string) < l:
        return False
    for i in range(l - 1):
        x = pattern[i]
        y = pattern[i + 1]
        last = string.rindex(x)
        first = string.index(y)
        if last == -1 or first == -1 or last > first:
            return False
    return True
```

### Minimum Window Subsequence

```python
# dp[i][j] = minimum substring length end at S[j] which contains subsequence of T[:i]
  	class Solution:
        def minWindow(self, s1: str, s2: str) -> str:
            m, n = len(s1), len(s2)
            dp = [float('inf')] * (m + 1)
            for j in range(1, m + 1):
                if s1[j - 1] == s2[0]:
                    dp[j] = 1
                else:
                    dp[j] = dp[j - 1] + 1
            for i in range(2, n + 1):
                tmp = [float('inf')] * (m + 1)
                for j in range(1, m + 1):
                    if s1[j - 1] == s2[i - 1]:
                        tmp[j] = dp[j - 1] + 1
                    else:
                        tmp[j] = tmp[j - 1] + 1
                dp = tmp
            res = min(dp)
            if res == float('inf'):
                return ''
            for i in range(1, m + 1):
                if dp[i] == res:
                    return s1[i - res: i]
```

### Alien Dictionary
但是追加是输出所有topological sort的组合

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

### My Calendar I

```python
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False
class MyCalendar:
    def __init__(self):
        self.root = None
    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))
```

### My Calendar II

```python
class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []
    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
```

### Maximum Points You Can Obtain from Cards

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        windowSize = n - k
        s = sum(cardPoints[:windowSize])
        minSum = s
        for i in range(windowSize, n):
            s += cardPoints[i] - cardPoints[i - windowSize]
            minSum = min(minSum, s)
        return sum(cardPoints) - minSum
```

### Maximum Score from Performing Multiplication Operations

```python
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        def dp(l, i):
            if (l, i) in mem:
                return mem[(l, i)]
            if i == m: 
                return 0
            pickLeft = dp(l + 1, i + 1) + nums[l] * multipliers[i]
            pickRight = dp(l, i + 1) + nums[n - (i - l) - 1] * multipliers[i]
            mem[(l, i)] = max(pickLeft, pickRight)
            return mem[(l, i)]
        
        mem = {}
        n, m = len(nums), len(multipliers)
        return dp(0, 0)
```

### Redact fobid words

Redact fobid words in a large document. 给一个list，要求里面出现的单词mask掉（我用 xxx），但是万一单词本身就是 xxx 的话，怎么处理要跟面试官讨论好。 感觉这轮没啥难度就是怎么实现而已

```python
def fobid(filein, fileout, wordset):
    def check(s):
        tmp = s.split("\n")
        if len(tmp) == 1:
            return "#" * len(s) if s.lower() in wordset else s
        first, second = tmp
        return "#" * len(first) + '\n' + "#" * len(second) if s.replace("\n", "").lower() in wordset else s

    with open(filein) as fin, open(fileout, 'w') as fout:
        cur = []
        for l in fin:
            out = []
            for c in l:
                if c.isalpha() or c == "\n":
                    cur.append(c)
                else:
                    out.append(check("".join(cur)))
                    out.append(c)
                    cur = []
            fout.write("".join(out))
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

### 博物馆sensor
假设你要给一个走廊（m * n）装摄像头，走廊的尽头是博物馆，给你一些sensor和这些sensor的探测半径R, 要你确定sensor的coordinate以防止小偷通过走廊到达博物馆。 已知sensors = [(x1, y1, r1), (x2, y2,r2), (x3, y3,r2)], hallway: 长m， 宽n， 问这些sensor安装的组合能否防止小偷通过这个hallway到达尽头的博物馆

相交建图，求所有的cc，如果存在一个cc最高点到最低点占据所有位置，返回true

### blackjack 算概率
calculate the probs where the dealer will end in 16-21
递归直到 > 21过程中，如果落在16-21 给抽的次数的结果+1，sum(抽的次数的概率/总的次数)

### generate candy crush



### guess photo 

在一堆图片里找到一个target照片 但只能通过一个API来判断是不是target API会返回每个pixel有没有match 主要讨论围绕在怎么优化来提前return false

### Job Scheduler



### Warptext
wrapText("A long string of words", 10) -> ["A long", "string of", "words"] Now we have new line "\n" in the string. We want to add the new line when we encounter "\n".



### 平均分牌
已知有一共x张牌，要分给y个牌堆里面，然后牌的种类是k种。分完之后牌堆数量要尽量平均，差距不能大于1。另外每个牌堆里面的组合尽可能不一样。比如说第一个牌堆是1123456，那么后面的牌堆就尽可能不这么分。

### 平均下棋
8*8的棋盘，四个player，随机（uniform distribution）assign每个grid给每个player。followup是如果其中一个相邻的grid必须被assign给同一个player怎么做(周围的四个方向里至少其中任意一个必须assign给同一个player，并且保持uniform)

### Airplane Seat Assignment Probability

```python
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        return 1.0 if n == 1 else 0.5
```

### 包含某一点的最小环



### Minimum Knight Moves 
类似利扣 亿亿久期，给定的棋盘大小是固定的，8x8，问给定步数M，起始位置和目的位置，能否在规定的步数到达目的地。



### Parse Lisp Expression
类似利扣 旗散留 简化版，只有加减



### Peeking Iterator
```python
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.peeknum = self.it.next() if self.it.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.peeknum

    def next(self):
        """
        :rtype: int
        """
        ret = self.peeknum
        self.peeknum = self.it.next() if self.it.hasNext() else None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeknum is not None
```

### Same Tree
比较两个binary tree的中序遍历的string sequence是否相同，面试官要求一边做中序遍历，一边比较。这样只要找到第一个不match的地方就可以马上返回

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### House robber 二维
问了一个House Robber(LC 198)的二维推广版, 就是给一个 n x m 2d array, 每个位置代表房子的金额 >= 0, 如果偷了一个房子, 则周围八个房子都不能偷, 问能偷到的最大金额是多少? 

### Serialize/Deserialize Binary Tree
```python
class Codec:
    def serialize(self, root):
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

### Shrinkable String

按长度排序，从短向长，如果可以shrink，连线，从长度为1的所有点遍历，所有能访问的点，都是可以shrink的

### Insert Delete GetRandom O(1)

```python
class RandomizedSet:
    def __init__(self):
        self.list = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        last, idx = self.list[-1], self.dic[val]
        self.list[idx], self.dic[last] = last, idx
        del self.dic[val]
        del self.list[-1]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)

```

### Longest Line of Consecutive One in Matrix

```python
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        res = 0
        m, n = len(mat), len(mat[0])
        dp = [[[0,0,0,0] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1
                    dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1
                    dp[i][j][2] = dp[i - 1][j - 1][2] + 1 if i > 0 and j > 0 else 1
                    dp[i][j][3] = dp[i - 1][j + 1][3] + 1 if i > 0 and j < n - 1 else 1
                    res = max(res, max(dp[i][j]))
        return res
```

### Sort Transformed Array

```python
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = []
        for i in nums:
            n.append(a * i * i + b * i + c)
        res = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            fl, fr = n[l], n[r]
            if (a > 0) ^ (fl > fr):
                res.append(fr)
                r -= 1
            else:
                res.append(fl)
                l += 1
        return res[::-1] if a > 0 else res
```

### Pacific Atlantic Water Flow

followup 1：不用extra array， followup 2：假设从一点开始，print到达终点的路径。

```python
class Solution:
    def dfs(self, matrix, q):
        m = len(matrix)
        n = len(matrix[0])
        ret = set([])
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        while len(q) > 0:
            curx, cury = q.pop()
            ret.add((curx, cury))
            height = matrix[curx][cury]
            for dirx, diry in directions:
                tmpx, tmpy = dirx + curx, diry + cury
                if 0 <= tmpx < m and 0 <= tmpy < n and matrix[tmpx][tmpy] >= height:
                    if (tmpx, tmpy) not in ret:
                        q.append((tmpx, tmpy))
                        ret.add((tmpx, tmpy))
        return ret
    
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        q = []
        for i in range(m):
            q.append((i, 0))
        for i in range(n):
            q.append((0, i))
        pac = self.dfs(matrix, q)

        q = []
        for i in range(m):
            q.append((i, n - 1))
        for i in range(n):
            q.append((m - 1, i))
        atl = self.dfs(matrix, q)

        res = pac.intersection(atl)
        return [list(x) for x in res]
```

### Duplicate Number

### Range Sum Query 2D - Mutable

```python
class NumMatrix(object):
    def __init__(self, matrix):
        m = len(matrix)
        if m == 0:
            self.matrix = []
            return
        n = len(matrix[0])
        self.matrix = matrix
        self.m = m
        self.n = n
        self.data = [[0 for i in range(n + 1)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                self.data[i][j + 1] = self.data[i][j] + matrix[i][j]

    def update(self, row, col, val):
        t = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for i in range(col, self.n):
            self.data[row][i + 1] += t

    def sumRegion(self, row1, col1, row2, col2):
        res = 0
        data = self.data
        for i in range(row1, row2 + 1):
            res += data[i][col2 + 1] - data[i][col1]
        return res
```

### Shortest Path in a Grid with Obstacles Elimination

```python
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        k = min(k, m + n - 3)
        visited = set([(0, 0, k)])
        q = collections.deque([(0, 0, k)])
        step = 0
        while len(q) > 0:
            step += 1
            cnt = len(q)
            for _ in range(cnt):
                x, y, rest = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                            if nx == m - 1 and ny == n - 1:
                                return step
                            q.append((nx, ny, rest))
                            visited.add((nx, ny, rest))
                        elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                            q.append((nx, ny, rest - 1))
                            visited.add((nx, ny, rest - 1))
        return -1
```

### Meeting Room

最近常见的CPU task，每个task有start time和end time，需要不同个数的cpu，问给的CPU数量够不够。Follow up：如果input太多并且不按时间排序怎么做。(meeting room)
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


### Rotting Oranges
Follow up：如果有一个位置需要感染两次才能变化怎么做。
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        m, n = len(grid), len(grid[0])
        q = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] ==  2:
                    q.add((i, j))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        while q:
            tmp = set()
            for curx, cury in q:
                for dirx, diry in directions:
                    tx, ty = curx + dirx, cury + diry
                    if 0 <= tx < m and 0 <= ty < n and grid[tx][ty] == 1:
                        tmp.add((tx, ty))
                        grid[tx][ty] = 2    
            q = tmp
            if q:
                res += 1
                fresh -= len(q)
        
        return res if fresh == 0 else -1
```


### 铺设光缆
有n个城市，在他们之间铺光缆，给出城市之间铺光缆的cost，问可以连接所有城市最小的cost Follow up：如果要返回最短的铺设线路怎么做。

```python
class MST:
    def __init__(self, n, graph):
        self.graph = sorted(graph, key=lambda x: x[2])
        self.rank = defaultdict(int)
        self.parent = {}
        self.n = n
        for i in range(n):
            self.parent[i] = i

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            else:
                self.parent[p1] = p2
                if self.rank[p1] == self.rank[p2]:
                    self.rank[p2] += 1

    def kruscal(self):
        edge = 0
        ct = 0
        res = []
        while ct < self.n - 1:
            u, v, w = self.graph[edge]
            edge += 1
            x = self.find(u)
            y = self.find(v)
            if x != y:
                ct += 1
                res.append([u, v, w])
                self.union(u, v)
        return sum([w for _, _, w in res])
```

### Count Square Submatrices with All Ones

Follow up：如果input是invalid的话要throw什么exception。语言Java。
```python
# dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1 if dp[i - 1][j - 1] == 1
#          = 0 else
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [matrix[0][i] for i in range(n)]
        res = sum(dp)
        for i in range(1, m):
            tmp = [matrix[i][0]]
            for j in range(1, n):
                if matrix[i][j]:
                    tmp.append(min(tmp[-1], dp[j], dp[j - 1]) + 1)
                else:
                    tmp.append(0)
            res += sum(tmp)
            dp = tmp[:]
        return res
```

### top K values in a datastream

### 多米诺骨牌

一堆多米諾骨牌在一个ordered list里面，每个骨牌有俩数，从0到六。先问能不能从头到尾连起来，两个骨牌能练假如说第一个尾数和第二个的头数是一样的。（trivial）follow up: 现在这个list不是ordered。现在能不能put them in some order，让他们变成能够从头到尾连起来。（跪了）

把每个骨牌拆开，并建立两个dummynode，判断欧拉路

### Point in Polygon


https://en.m.wikipedia.org/wiki/Point_in_polygon

https://leetcode.com/discuss/interview-question/algorithms/125032/points-contained-in-a-polygon

https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/


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

### 抽排 Stone Game III
```python
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
```

### 修改机场代码 The Most Similar Path in a Graph
有一些飞机场，代号都是三个字母，有些飞机场之间有航线，给出一个字符串序列，每个字符串都是三个字符，问至少修改其中多少个字符可以使这个字符串序列成为合理的行程, i.e.相邻的两个飞机场之间是有航线的

```python
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], tp: List[str]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        m = len(tp)
        dp = [[m] * n for _ in range(m)]
        prev = [[0] * n for _ in range(m)]
        
        for v in range(n):
            dp[0][v] = (names[v] != tp[0])
        for i in range(1, m):
            for v in range(n):
                for u in graph[v]:
                    if dp[i-1][u] < dp[i][v]:
                        dp[i][v] = dp[i-1][u]
                        prev[i][v] = u
                dp[i][v] += (names[v] != tp[i])
                
        path, min_dist = [0], m
        for v in range(n):
            if dp[-1][v] < min_dist:
                min_dist = dp[-1][v]
                path[0] = v
        for i in range(m - 1, 0, -1):
            u = prev[i][path[-1]]
            path.append(u)
            
        return path[::-1]
```

### 二叉树错误节点
有一个指针是错的导致某node有两个parent，找到他并修改之。

### Strobogrammatic Number II
```python
class Solution(object):
    def findStrobogrammatic(self, n):
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

### Read N Characters Given Read4

```python
def read(self, buf, n):
    idx = 0
    while n > 0:
        buf4 = [""]*4
        l = read4(buf4)
        if not l:
            return idx
        for i in range(min(l, n)):
            buf[idx] = buf4[i]
            idx += 1
            n -= 1
    return idx
```



### 翻硬币
给一个硬币面朝上朝下的0/1一维数组，求通过一次翻转(翻转起止位置自己定)能够得到的最大1的个数 问题改为2D数组，问通过一次sub-matrix翻转能够得到的最大1的个数

先把1变成-1，0变成1

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]
        for i in range(1, len(nums)):
            tmp = cur + nums[i]
            cur = nums[i] if nums[i] > tmp else tmp
            if cur > res:
                res = cur
        return res
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

### Stram median
followup 就是有一个infinite data stream，如何做到去掉5th percentile之前的部分和95th percentile之后的部分，剩下部分的median

```python
class MedianFinder(object):
    def __init__(self):
        self.small = []
        self.large = []
    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return self.large[0]
```

### Serialize and Deserialize N-ary Tree



### 有效前缀
两个机器人玩游戏， 每次append 一个字母，组成的现有字符如果是一个有效的单词的前缀就继续游戏， 如果不是有效率前缀或者是有效单词就输了，

```python
class Trie:
    def __init__(self, wordlist):
        self.root = {}
        for word in wordlist:
            self.insert(word)
        self.gen(self.root)
        self.cur = self.root

    def gen(self, node):
        if '#' in node:
            node["rec"] = 'win'
            return False
        for c in node:
            if self.gen(node[c]):
                node["rec"] = c
                return False
        node["rec"] = "lose"
        return True

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def play(self, c):
        if c not in self.cur:
            self.cur = self.root
            return False
        self.cur = self.cur[c]
        if '#' in self.cur:
            self.cur = self.root
            return False
        return True

    def get_rec(self):
        return self.cur['rec']
```

### Word Search
26个字母组成一个矩阵，输入是矩阵的宽度， 给一个单词，从A开始、怎么走把这个单词打印出来

### 多少点共圆
给二维平面上的一堆点，求圆的边界最多能碰到多少个点
https://leetcode.com/discuss/interview-question/300335/Google-Onsite-Circle-with-most-points-in-its-circumference/282130

确定两个点，取一次c，构成一个圆，去掉所有在圆上的点，继续

### Maximum Sum of Two Non-Overlapping Subarrays

要求求最大和最小值

```python
	def maxSumTwoNoOverlap(self, A, L, M):
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res
```



### 但是是OOD。设计一个科学计算单位类，



### 文件系统求size
给一个map来表示一个filesystem，key是node ID，value是一个object，object可以是file，file有size，也可以是directory，directory有children objects。写一个function求一个node下面的total size。



### matrix path cost
给一个matrix，求从top left到bottom right的cost，如果比current position低或者一样没有cost，如果比current position高，高多少要pay的cost就是多少，dijkstra就行，不过面试官告诉我standard dijkstra会waste memory！需要用一个cost matrix来optimize。。。真智商碾压。follow up是如果现在不用爬山pay cost，而是可以调整一个cell的高度，调高多少cost多少，从top left到bottom right的min cost

### Path With Minimum Effort

```python
class Solution:
    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        distances = defaultdict(lambda: float('inf'))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = []
        heappush(q, (0, 0, 0))
        while q:
            effort, curx, cury = heappop(q)
            if (curx, cury) == (m - 1, n - 1):
                return effort
            for dx, dy in dirs:
                tx, ty = curx + dx, cury + dy
                if 0 <= tx < m and 0 <= ty < n:
                    tmp = max(effort, abs(heights[tx][ty] - heights[curx][cury]))
                    if distances[(tx, ty)] > tmp:
                        distances[(tx, ty)] = tmp
                        heappush(q, (tmp, tx, ty))
```

### Island Perimeter

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i + 1 < m and grid[i + 1][j] == 1:
                        res -= 2
                    if j + 1 < n and grid[i][j + 1] == 1:
                        res -= 2
        return res
```

### Call Center

一个很老的call center，只能同时接听三个客服电话，现在给一堆log，电话打入时间和结束时间，找出给定时间段内所有超过系统负载的次数次数

1. Given a positive integer array. Partition it into N disjoint sets and make sure any sum of any set not exceeding given target M. Return such minimal N.

2. Given List<String> A. len(A) very large. A lot of queries with String target against all strings in A.   Return all strings in A with target as substring. Results order: supposed the queried string as B. first sort by index in B and then by B itself alphabetical order. best complexity for query?
3. Given a integer range. could be negative integers. Caculate how many integers in this range which binary representation (64 bits at most) has N 1s when N is some Fibonacci number.   don`t use library function to caculate binary representation. Digit DP in O(1)?
4. Assume an array A, at first, you have no information about A. there will be some queris <start, end, odd/even> in sequence. each query means: A[start:end+1] is odd/even. Detect the first conflict.   Example: <2, 14, odd>, <8, 14, even>, <2, 7, even>. when first and second comes in, we know 2->7 has to be odd-even=odd.   but when the third comes in, it is even (conflict with existing information about A)5. N objects 1 -> N in a 2-D grid. Given a set of rules as <first, second, left/right/up/down> (the first is on left/right/up/down of the second).   Return any one of possible arragement of those N objects.   Example: N=3, <1, 3, right>, <2, 3, right>, <1, 2, up>, <1, 2, left>, <2, 3, up>.   one possible result: ["*1*", "**2", "3**"], * is empty.

###  String Encode

Original = "abcdkkkkkkkkkkd55s" encode to "abcd11xkd55s"

### Distribute Coins in Binary Tree

```python
class Solution(object):
    def distributeCoins(self, root):
        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.res += abs(L) + abs(R)
            return node.val + L + R - 1

        self.res = 0
        dfs(root)
        return self.res
```

### Longest Substring with At Least K Repeating Characters

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(1, len(set(s)) + 1):
            times = [0] * 26
            l = r = ct = dif_ct = 0
            while r < len(s):
                ind = ord(s[r]) - ord('a')
                times[ind] += 1
                if times[ind] == 1:
                    dif_ct += 1
                if times[ind] == k:
                    ct += 1
                r += 1
                
                while l < r and dif_ct > i:
                    ind = ord(s[l]) - ord('a')
                    if times[ind] == k:
                        ct -= 1
                    if times[ind] == 1:
                        dif_ct -= 1
                    times[ind] -= 1
                    l += 1
                if dif_ct == ct == i:
                    res = max(res, r - l)
        return res
```

### Reformat phone number

```python
class Solution:
    def reformatNumber(self, number: str) -> str:
        res = []
        number = number.replace(' ','').replace('-', '')
        res.append(number[0])
        for i in range(1, len(number)):
            if i % 3 == 0:
                res.append('-')
            res.append(number[i]);
        l = len(res)
        if (res[l - 2] == '-'):
            res[l - 2], res[l - 3] = res[l - 3], res[l - 2]
        return ''.join(res)
```

### Sum of Subsequence Widths

```python
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(nums)
        nums.sort()
        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)
        ans = 0
        for i, x in enumerate(nums):
            ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
        return ans
```

### Random Pick Index

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.l = len(nums)

    def pick(self, target: int) -> int:
        cnt = 0
        res = None
        for i in range(self.l):
            if self.nums[i] == target:
                if cnt < 1:
                    res = i
                else:
                    r = random.randint(0, cnt)
                    if r < 1:
                        res = i
                cnt += 1
        return res
```

### 分隔字符串，
要么分割成单个字符，要么如果这部分可以用之前已经分割的部分再加上一个新的字符构造。所有子字符串必须最长。例子: gooogle -> 'g' , 'o', 'oo', 'gl', 'e'.

### Log file 求时间
有一个logfile，里面有每个method的开始和结束时间，算每个method运行的时间。
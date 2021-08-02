## Max Area of Island

变体，求相同value的，讨论复杂度

```python
def dfs(M, i, j):
    m, n = len(M), len(M[0])
    q = [(i, j)]
    color = M[i][j]
    M[i][j] = -1
    area = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        curx, cury = q.pop()
        area += 1
        for dirx, diry in directions:
            tmpx, tmpy = curx + dirx, cury + diry
            if 0 <= tmpx < m and 0 <= tmpy < n and M[tmpx][tmpy] == color:
                q.append((tmpx, tmpy))
                M[tmpx][tmpy] = -1
    return area

def max_island(M):
    m, n = len(M), len(M[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if M[i][j] != -1:
                res = max(res, dfs(M, i, j))
    return res
```

## K Closest Points to Origin

如果这是个rest api,需要考虑什么

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

## Count All Valid Pickup and Delivery Options

1. 给定一个序列有pickup和delivery ，check是不是valid。取货要在送货之前，所有单最后都要送货完成
2. 给定N, 打印所有valid序列
3. 推导计算valid序列数量的公式

第一问验证valid sequence 同一个order先p后d 不可重复pd 所有order必须有p有d
第二问 给定order数量 generate所有valid sequence

```python
def valid_sequence(sequence):
    s = dict()
    rem = 0
    for seq in sequence:
        number = seq[1:]
        if seq[0] == 'P':
            if number in s:
                return False
            s[number] = 1
            rem += 1
        else:
            if number not in s or s[number] != 1:
                return False
            s[number] -= 1
            rem -= 1
    return rem == 0
```

```python
def generate_orders(n):
    res = [["P1", "D1"]]
    for i in range(2, n + 1):
        tmp = []
        for item in res:
            for j in range(len(item) + 1):
                for k in range(j, len(item) + 1):
                    tmp.append(item[:j] + ["P" + str(i)] + item[j: k] + ["D" + str(i)] + item[k:])
        res = tmp
    return res
```

```python
class Solution:
    def countOrders(self, n: int) -> int:
        res, mod = 1, 10**9 + 7
        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * i % mod
        return res
```

## quick select

```python
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        index = partition(arr, l, r)
        if index - l == k - 1:
            return arr[index]
        if index - l > k - 1:
            return kthSmallest(arr, l, index - 1, k)
        return kthSmallest(arr, index + 1, r,
                            k - index + l - 1)
```

## calendar bookings

1. 给了一个List的calendar bookings， 要求返回所有在区间a 到 b内，大于duration的空闲时间段。

bookings = [[0, 10], [5,15], [20, 30], [40, 50]],
a = -5,
b = 60,
duration = 8
结果：[[30,40], [50, 60]]

```python
import bisect
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for interval in intervals[1:]:
        if res[-1][1] >= interval[0]:
            res[-1][1] = max(interval[1], res[-1][1])
        else:
            res.append(interval)
    return res

def booking(intervals, a, b, duration):
    merged = merge(intervals)
    ind = bisect.bisect_left(merged, [a])
    res = []
    left = a if ind == 0 else max(a, intervals[ind - 1][1])
    for interval in merged[ind:]:
        if interval[0] > b:
            if interval[0] - left >= duration:
                res.append([left, b])
            break
        if interval[0] - left >= duration:
            res.append([left, interval[0]])
        left = interval[1]
    if b - left >= duration:
        res.append([left, b])
    return res
```

## schedule meeting

给一个人的list of meetings和一个时间范围的start, end和 duration, 输出在时间范围内大于duration的空闲slot
followup不太一样 是给一群人的list of free slots, 一个时间范围的start, end和 duration, 在时间范围内所有人共同的free slots里找长度大于duration的

## Merge Intervals

物流的变形，变成了calendar找空的时间来schedule会以及加了start time和end time，要求自己想edge case。

[3, 20], [-2, 0], [0, 2], [16, 17], [19, 23], [30, 40], [27, 33].
可以meeting 的時間 ie. [-5, 50]
找出free meeting time
可以先用lc五路找出merged meeting. 在loop一遍找出所有free meeting time

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

## Shortest Path with Alternating Colors

```python
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        G = [[[], []] for i in range(n)]
        for i, j in red_edges: 
            G[i][0].append(j)
        for i, j in blue_edges: 
            G[i][1].append(j)
        res = [[0, 0]] + [[n * 2, n * 2] for i in range(n - 1)]
        q = deque([[0, 0], [0, 1]])
        while q:
            i, c = q.popleft()
            for j in G[i][c]:
                if res[j][c] == n * 2:
                    res[j][c] = res[i][1 - c] + 1
                    q.append([j, 1 - c])
        return [x if x < n * 2 else -1 for x in map(min, res)]
```

## Valid Sudoku

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(lambda:set())
        rows = defaultdict(lambda:set())
        grids = defaultdict(lambda:set())
        for i in range(0,9):
            for j in range(0,9):
                if  board[i][j] == '.':
                    continue
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                if board[i][j] in grids[10*(i//3)+j//3]:
                    return False
                grids[10*(i//3)+j//3].add(board[i][j])
        return True
```

## Sudoku Solver

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve(board, pos):
            for i, j in pos:
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if check(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if solve(board, pos):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
            return True
        
        def check(board, row, col, c):
            for i in range(9):
                if c in (board[i][col], board[row][i], board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3]):
                    return False
            return True
    
        pos = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    pos.append((i, j))
        solve(board, pos)
```

## Course Schedule II

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

## Missing Ranges

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        pre = lower - 1
        for cur in nums + [upper + 1]:
            if pre + 1 < cur:
                res.append("%s->%s" % (pre + 1, cur - 1) if pre + 1 != cur - 1 else str(cur - 1))
            pre = cur
        return res
```

## Employee Free Time

输出不光是free timeslot，还需要那个timeslot哪几个employee是free的

额外有一个startTime, endTime and minDuration. 需要单独判断一下
end = min(pos.first : endTime);start = max(start, startTime);if (end - start >= minDuration) {
      res.push_back({start, end});
}

```python
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, pre = [], ints[0]
        for i in ints[1:]:
            if i.start <= pre.end and i.end > pre.end:
                pre.end = i.end
            elif i.start > pre.end:
                res.append(Interval(pre.end, i.start))
                pre = i
        return res
```

## Maximum Profit in Job Scheduling

```python
def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
```

## Accounts Merge

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

*Problem Statement: Consolidate and eliminate duplicates in the list of usernames and their email addresses.*

https://www.1point3acres.com/bbs/thread-770584-1-1.html

## Topology sort

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

## Meeting Scheduler

```python
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        p1 = p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            intersect_right = min(slots1[p1][1], slots2[p2][1])
            intersect_left = max(slots1[p1][0],slots2[p2][0])
            if intersect_right - intersect_left >= duration:
                return [intersect_left, intersect_left + duration]
            if slots1[p1][1]< slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []
```

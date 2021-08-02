### Basic Calculator

- `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.

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

```python
class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]
        sign = 1
        res = 0
        s.replace(" ", "")
        cur = 0
        for c in s + '+':
            if c.isdigit():
                cur = cur * 10 + int(c)
            else:
                res += cur * sign
                cur = 0
            if c == '+':
                sign = ops[-1]
            elif c == '-':
                sign = -ops[-1]
            elif c == '(':
                ops.append(sign)
            elif c == ')':
                ops.pop()
        return res
```

```python
class Solution:
    def calculate(self, s: str) -> int:
        signstack = []
        pool = []
        tmp = 0
        s.replace(" ", "")
        flag = True
        for c in s:
            if c in "1234567890":
                tmp = tmp * 10 + int(c)
                flag = True
            elif c in "+-":
                if flag:
                    pool.append(tmp)
                tmp = 0
                while True:
                    if len(signstack) == 0 or signstack[-1] == "(":
                        signstack.append(c)
                        break
                    else:
                        pool.append(signstack.pop())

            elif c in "*/":
                if flag:
                    pool.append(tmp)
                tmp = 0
                while True:
                    if len(signstack) == 0 or signstack[-1] == "(":
                        signstack.append(c)
                        break
                    elif signstack[-1] in "*/":
                        pool.append(signstack.pop())
                    else:
                        signstack.append(c)
                        break
            elif c == "(":
                signstack.append('(')
            elif c == ")":
                if flag:
                    pool.append(tmp)
                tmp = 0
                flag = False
                while True:
                    if signstack[-1] != '(':
                        pool.append(signstack.pop())
                    else:
                        signstack.pop()
                        break
        if flag:
            pool.append(tmp)
        pool += signstack[::-1]
        cal = []
        for it in pool:
            if isinstance(it, int):
                cal.append(it)
            else:
                op2 = cal.pop()
                op1 = cal.pop()
                if it == '+':
                    cal.append(op1 + op2)
                elif it == '-':
                    cal.append(op1 - op2)
                elif it == '*':
                    cal.append(op1 * op2)
                else:
                    cal.append(op1 / op2)
        return cal[0]
```

### Closest Subsequence Sum

```python
class Solution:
     def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        a1 = self.func(nums[ :n//2])
        a2 = self.func(nums[n//2: ])
        a1.sort()
        a2.sort()
        res = 0x3f3f3f3f
        i, j = 0, len(a2)- 1
        while i < len(a1) and -1 < j:
            cur_sum = a1[i] + a2[j]
            res = min(res, abs(cur_sum - goal))
            #贪心的策略
            if cur_sum > goal:              #超了，大的就小一点              
                j -= 1
            elif cur_sum < goal:            #小了，小的就大一点
                i += 1
            else:                           #相等了，直接就是0了
                return 0
        return res

    def func(self, nums: List[int]) -> List[int]:   #枚举所有情况的和
        n = len(nums)
        res = [0 for _ in range(1 << n)]    #2**n种可能
        for i in range(n):
            for j in range(1<<i):
                res[(1<<i) + j] = nums[i] + res[j]
        return res
```

### Course Schedule II

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

### Continuous Subarray Sum

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        tmp = 0
        d = {0: -1}
        for i in range(len(nums)):
            tmp = (tmp + nums[i]) % k
            if tmp in d:
                if i - d[tmp] > 1:
                    return True
            else:
                d[tmp] = i
        return False
```

### Decode String

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = cur_str = ''
        for c in s:
            if c == '[':
                stack.append(cur_str)
                stack.append(int(cur_num))
                cur_num = cur_str = ''
            elif c == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + cur_str * num
            elif c.isdigit():
                cur_num += c
            else:
                cur_str += c
        return cur_str
```

### Decode Ways

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l = len(s)
        dp = [0] * (l + 1)
        dp[-1] = 1
        dp[-2] = 0 if s[-1] == '0' else 1
        for i in range(l - 2, -1, -1):
            if s[i] == '0':
                continue
            dp[i] = dp[i + 1] + dp[i + 2] if int(s[i: i+2]) <= 26 else dp[i + 1]
        return dp[0]
```

### Decode Ways 2

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = 9 * e0 + 9 * e1 + 6 * e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0
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

```python
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
```

### Minimum Genetic Mutation

```python
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        wordList, beginWord, endWord = set(bank), start, end
        l = len(beginWord)
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i + 1:]
                d[s] += [word]

        q = deque()
        q.append((beginWord, 1))
        visit = set()
        while q:
            now, dis = q.popleft()
            if now in visit:
                continue
            visit.add(now)
            for i in range(l):
                tmp = now[:i] + '_' + now[i + 1:]
                neb = d[tmp]
                for v in neb:
                    if v in visit:
                        continue
                    if v == endWord:
                        return dis
                    q.append((v, dis + 1))
        return -1
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

### [Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4)

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

### [Read N Characters Given Read4 II - Call multiple times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times)

```python
class Solution:
    def __init__(self):
        self.q = collections.deque()
    
    def read(self, buf: List[str], n: int) -> int:
        i = 0  
        buf4 = [''] * 4
        while n > 0: # number of chars left to read
            if self.q:
                buf[i] = self.q.popleft()
                i += 1
                n -= 1
            else:
                readn = read4(buf4)
                if readn == 0: # file exhausted
                    break
                self.q.extend(buf4[:readn])
        return i
```

### [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner)

```python
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set())
    
    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))
        
        for k in range(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x
```



### Sliding Window Median

```python
class DualHeap:
    def __init__(self, k: int):
        # 大根堆，维护较小的一半元素，注意 python 没有大根堆，需要将所有元素取相反数并使用小根堆
        self.small = list()
        # 小根堆，维护较大的一半元素
        self.large = list()
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = collections.Counter()
        self.k = k
        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0

    # 不断地弹出 heap 的堆顶元素，并且更新哈希表
    def prune(self, heap: List[int]):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                break
    
    # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
    def makeBalance(self):
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.makeBalance()

    def erase(self, num: int):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.makeBalance()

    def getMedian(self) -> float:
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0] + self.large[0]) / 2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)
        
        ans = [dh.getMedian()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.getMedian())
        return ans
```

### Serialize and Deserialize BST

```python
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ret = []
        def preorder(root):
            if root:
                ret.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ' '.join(map(str, ret))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nums = deque(int(n) for n in data.split())
        def build(mmin, mmax):
            if nums and mmin < nums[0] < mmax:
                n = nums.popleft()
                node = TreeNode(n)
                node.left = build(mmin, n)
                node.right = build(n, mmax)
                return node
        return build(float('-inf'), float('inf'))
```

### [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(root):
            if root:
                data.append(str(root.val))
                doit(root.left)
                doit(root.right)
            else:   
                data.append('#')
                
        data = []
        doit(root)
        return ' '.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val = next(d)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = doit()
                node.right = doit()
            return node
            
        d = iter(data.split(' '))
        return doit()
```

### Spiral Matrix

```python
res = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        for i in range(m):
            matrix[i] = ['#'] + matrix[i] + ['#']
        matrix = [['#'] * (n+2)] + matrix + [['#'] * (n+2)]
        
        nowx = 1
        nowy = 1
        dir = 0
        t = m * n
        while len(res) < t:
            res.append(matrix[nowx][nowy])
            matrix[nowx][nowy] = '#'
            if dir == 0:
                nowy += 1
                if matrix[nowx][nowy] == '#':
                    dir = 1
                    nowy -= 1
                    nowx += 1
            elif dir == 1:
                nowx += 1
                if matrix[nowx][nowy] == '#':
                    dir = 2
                    nowx -= 1
                    nowy -= 1
            elif dir == 2:
                nowy -= 1
                if matrix[nowx][nowy] == '#':
                    dir = 3
                    nowy += 1
                    nowx -= 1
            else:
                nowx -= 1
                if matrix[nowx][nowy] == '#':
                    dir = 0
                    nowx += 1
                    nowy += 1
        return res
```

### Surrounded Regions

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        stack = []
        for i in range(m):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if board[i][n - 1] == 'O':
                stack.append((i, n - 1))
        for i in range(1, n - 1):
            if board[0][i] == 'O':
                stack.append((0, i))
            if board[m - 1][i] == 'O':
                stack.append((m - 1, i))
        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = '#'
                stack += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
        board[:] = [['XO'[c == '#'] for c in row] for row in board]
```

### Trie

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
```

### Text Justification

```python
class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, cur, numLetter = [], [], 0
        for w in words:
            if numLetter + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append(cur[0] + ' ' * (maxWidth - numLetter))
                else:
                    space = maxWidth - numLetter
                    gap, extra = divmod(space, len(cur) - 1)
                    for i in range(extra):
                        cur[i] += ' '
                    res.append((' ' * gap).join(cur))
                cur, numLetter = [], 0
            cur.append(w)
            numLetter += len(w)
        res.append(' '.join(cur) + ' ' * (maxWidth - numLetter - len(cur) + 1))
        return res
```



### [Word Pattern II](https://leetcode.com/problems/word-pattern-ii)

```python
def wordPatternMatch(self, pattern, str):
    return self.dfs(pattern, str, {})

def dfs(self, pattern, str, dict):
    if len(pattern) == 0 and len(str) > 0:
        return False
    if len(pattern) == len(str) == 0:
        return True
    for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
        if pattern[0] not in dict and str[:end] not in dict.values():
            dict[pattern[0]] = str[:end]
            if self.dfs(pattern[1:], str[end:], dict):
                return True
            del dict[pattern[0]]
        elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
            if self.dfs(pattern[1:], str[end:], dict):
                return True
    return False
```



### Word Search

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, p):
            if p == l:
                return True
            for dirx, diry in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and flag[curx][cury] and board[curx][cury] == word[p]:
                    flag[curx][cury] = False
                    if dfs(curx, cury, p + 1):
                        flag[curx][cury] = True
                        return True
                    flag[curx][cury] = True
            return False
        
        m, n = len(board), len(board[0])
        l = len(word)
        flag = [[True] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag[i][j] = False
                    if dfs(i, j, 1):
                        return True
                    flag[i][j] = True
        return False
```

### Word Search II

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, root):
            letter = board[x][y]
            cur = root[letter]
            word = cur.pop('#', False)
            if word:
                res.append(word)
            board[x][y] = '*'
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            board[x][y] = letter
            if not cur:
                root.pop(letter)
        
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res
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

### Ways to Split Array Into Three Subarrays

```python
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        res, sums = 0, [0]
        for num in nums:
            sums.append(sums[-1] + num)
        n = len(nums)
        for i in range(n - 2):
            left_sum, rest_sum = sums[i + 1], sums[n] - sums[i+1]
            if left_sum * 2 > rest_sum:
                break
            first = bisect.bisect_left(sums, left_sum * 2, i + 2, n)
            last = bisect.bisect_right(sums, left_sum + rest_sum // 2, i + 2, n)
            res += last - first
        return res % (10**9 + 7)
```

### Union Find

```python
				def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]
            
        def union(v1, v2):
            p1 = find(v1)
            p2 = find(v2)
            if p1 not in rank:
                rank[p1] = 0
            if p2 not in rank:
                rank[p2] = 0
            if p1 != p2:
                self.res -= 1
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                else:
                    parent[p1] = p2
                    if rank[p1] == rank[p2]:
                        rank[p2] += 1
          parent = {}
	        rank = {}
```

### Binary Index Tree

```python
				def update(k):
            while k <= limit:
                range_sum[k] += 1
                k += k & -k
        
        def query(k):
            ret = 0
            while k:
                ret += range_sum[k]
                k -= k & -k
            return ret
```
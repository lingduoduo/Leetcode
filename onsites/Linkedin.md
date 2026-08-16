先说整体感受。领英的面试节奏比较克制，不像有些家一轮塞两三道题。基本是一轮一道主题目，把它做扎实，然后往数据规模上延伸。面试官普遍很有耐心，会等你自己把话说完，不太打断。另外有一轮是 Host Manager，不考代码，专门聊经历和文化契合，这一轮的比重比我预想的要高。
以下按面试顺序记录。
一、Coding 第一轮
题目是舞灵，实现 pow(x, n)。
看起来是道简单题，但面试官关心的完全不是能不能做出来，而是几个细节：
我先问了 n 是否可能为负、x 是否可能为 0、结果是否会溢出。面试官说 n 可能为负，其余按常规处理。
直接循环乘 n 次是 O(n)，我说了这个 baseline，然后给出快速幂的 O(log n) 解法。
递归和迭代两种写法都被要求写了。递归版更好读，迭代版不用担心栈深度。
最后一个坑是 n 取 INT_MIN 时，取负数会溢出。我一开始没注意到，是面试官问「n 等于最小的负整数会怎样」才发现的。处理办法是先转成 long，或者单独处理这一种情况。
结论：这一轮考的不是算法难度，是严谨程度。建议大家写简单题的时候也把边界过一遍。
二、Coding 第二轮
题目是溜舞拔，在一个有序数组里找离 x 最近的 k 个数，结果要保持有序。
我给了两个方案并做了比较：
方案一，先二分找到 x 的插入位置，然后左右两个指针向外扩张 k 次，每次选距离更近的一侧。复杂度 O(log n + k)。
方案二，直接对左边界做二分，判断条件是比较 A[mid] 和 A[mid+k] 到 x 的距离。复杂度 O(log(n-k) + k)。
面试官让我把方案二写出来，并且解释清楚那个判断条件为什么成立。这里我讲了一段：如果 A[mid] 离 x 比 A[mid+k] 更远，说明窗口应该整体右移。他追问了一句「相等的时候往哪边走」，我说往左，因为题目要求相同距离取较小的数。
follow up 有两个：
如果数组不是有序的呢。答：那就退化成用大小为 k 的堆，O(n log k)。
如果数组特别大、大到放不进内存呢。答：可以先用索引或者分块的方式定位到大致区间，只把那一段读进内存。这里我答得不算深入。
三、Coding 第三轮
这一轮题目不在刷题网上，是一道设计感更强的题。
题目：给一个非常大的有序数组，统计里面有多少个不同的值。已知不同值的个数 k 远小于数组长度 n。
我一开始给的是线性扫描 O(n)，面试官说「n 是十亿级别，k 只有几百，还能更快吗」。
想通之后思路是这样的：既然相同的值是连成一段的，就没必要一个个走。可以从当前值出发，用二分找到这一段的右边界，直接跳到下一段。这样总复杂度是 O(k log n)，当 k 远小于 n 的时候比 O(n) 快得多。
面试官还提了另一种等价写法，用分治：
def countUnique(arr, start, end): if start == end: return 1 if arr[start] == arr[end]: return 1 mid = (start + end) // 2 if arr[mid] == arr[mid+1]: return countUnique(arr, start, mid) + countUnique(arr, mid+1, end) - 1 else: return countUnique(arr, start, mid) + countUnique(arr, mid+1, end)
两种写法的核心是同一件事：利用有序性，让相同的元素一次跳过而不是逐个访问。他让我分析了分治写法在最坏情况（全都不同）下会退化成 O(n)，这个我答上来了。
四、System Design
题目是设计信息流（feed）。
我按下面的顺序推进：
需求澄清。用户量级、平均关注数、读写比例、时效性要求（是否必须秒级看到新内容）、要不要做排序还是纯按时间倒序。面试官说读远大于写，允许秒级延迟，需要做排序但排序模型本身不用展开。
核心矛盾。推模式（写扩散）读快写重，拉模式（读扩散）写轻读重。我说主体用推，因为读写比悬殊；但对关注者极多的大 V 用拉，避免一条内容扇出到几百万个收件箱。这就是常说的混合方案。
数据模型。用户表、关注关系表、内容表、收件箱表。收件箱只存内容 ID 和排序分，正文另外取，这样收件箱可以很轻。
被深挖的几个点：
收件箱要不要设上限。我说只保留最近若干条，历史内容走拉取，这样存储可控。
大 V 发文的扇出怎么削峰。答：异步队列 + 分批处理，允许延迟。
排序分怎么更新。答：写入时算一个基础分，读取时结合实时特征做一次轻量重排。
缓存怎么设计。答：活跃用户的收件箱常驻缓存，非活跃用户按需加载，用 LRU 淘汰。
最后聊了一致性。用户自己发的内容必须立刻在自己的 feed 里可见，这一点不能靠异步，需要读自己写的时候做特殊处理。
这一轮我准备得比较充分，推进得比较顺。
五、Host Manager
不考代码，四十五分钟全在聊。问题如下：
介绍一个你最近主导的项目，你的角色具体是什么
讲一次你和其他团队产生分歧的经历，最后怎么收场的
有没有过项目做到一半方向被改的情况
你收到过的最有价值的反馈是什么
你希望下一份工作里，哪些是现在这份工作给不了你的
前四个问题都是常规的，我按 STAR 准备的稿子基本能覆盖。第五个问题有点意外，感觉是在看动机是否真实、是不是只是想跳槽涨薪。我回答的时候讲了具体的技术方向而不是泛泛而谈，manager 明显更愿意接话了。
这一轮的追问密度不高，但每个问题都会问到「所以最后结果是什么」。建议把每个故事的结果部分想清楚，最好有可量化的东西。
几点总结
一、领英不追求题目难度，追求把一道题做透。五轮里没有一道 hard，但每道题的边界条件、复杂度、替代方案都被问了个遍。
二、简单题反而要更小心。第一轮那道 pow 如果不是面试官提醒，我就在溢出上栽了。
三、把「数据规模变大」当成默认 follow up。我这次三轮 coding 有两轮都问到了「如果放不进内存怎么办」。
四、Host Manager 轮不要当水轮准备。它在整体评估里的权重不低，而且问的东西和纯 BQ 不完全一样，会涉及动机和长期规划。
五、SD 轮建议先把混合方案的取舍讲清楚再往下铺，不要一上来就画组件图。

Round 1
第一轮是经典的数组处理题，题目是 LeetCode 56（Merge Intervals）。
整体难度不高，主要看基本功。核心思路是先按区间起点排序，再遍历合并重叠部分。真正拉开差距的是代码的“Pythonic”程度和边界处理，比如如何用 lambda 优雅排序、如何处理空输入或单元素区间。
这一轮面试官更看重你的代码是否简洁易读、逻辑是否清晰，以及写代码时有没有主动解释思路，而不是闷头写。
       
Round 2
第二轮会在基础算法上加一层“思维切换”的考察。题目是 LeetCode 235（BST 最近公共祖先）。
如果是标准的 BST，利用左小右大的特性直接迭代或递归就能快速定位。
Follow-up: 如果把这棵树换成没有顺序特性的普通二叉树怎么办？
这时候思路就要从“利用结构特性”切换到“通用遍历”，也就是 LeetCode 236 的解法，用后序遍历自底向上查找。很多同学容易卡在这里，因为需要快速从特例解法切换到通用解法，考察的是知识迁移能力。
       
Round 3
这一轮是整个面试的核心，题目是设计一个「本地体育资讯推荐系统」，但实际考察的是你对 LLM 应用落地（RAG） 的理解。
首先得讨论架构选型，比如是用 Azure AI Search 做向量检索，还是自己搭 Milvus；是用 Fine-tuning 还是 Prompt Engineering。接着会深入到模型部署层面，比如如何在保证效果的同时降低延迟，这里通常会涉及到量化（Quantization）、蒸馏（Distillation）等优化手段。
然后一定会聊到一个关键问题：Hallucination（模型幻觉）。你需要说明如何降低错误信息，比如通过引入检索增强（RAG）增加事实依据、增加校验层，甚至设计类似 Red Teaming 的机制去做输出审核。

### All O`one Data Structure

```python

```

### Check if One String Swap Can Make Strings Equal

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        tmp = []
        for x, y in zip(s1, s2):
            if x != y:
                tmp.append((x, y))
        return not tmp or len(tmp) == 2 and tmp[0][0] == tmp[1][1] and tmp[0][1] == tmp[1][0]
```

### Can Place Flowers

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed.extend([0, 0])
        for i in range(len(flowerbed) - 2):
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n
```

### [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii) 

```python
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorderTraversal(root):
            if not root:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
        
        data = inorderTraversal(root)
        l = 0
        r = len(data) - 1
        while (r - l + 1 > k):
            if target - data[l] > data[r] - target:
                l += 1
            else:
                r -= 1
        return data[l: r + 1]
```

### Evaluate Reverse Polish Notation

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif t == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif t == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif t == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(float(num1) / num2))
            else:
                stack.append(int(t))
        return stack.pop()
```

### Design HashMap

```python
class Node:
    def __init__(self, key, value, nextNode=None):
        self.key = key
        self.val = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.head = Node(0, 0)
    def get(self, key):
        cur = self.head.next
        while cur:
            if cur.key == key:
                return cur
            cur = cur.next
        return None
    def insert(self, key, val):
        tmp = self.get(key)
        if tmp:
            tmp.val = val
        else:
            node = Node(key, val, self.head.next)
            self.head.next = node
    def delete(self, key):
        pre = self.head
        cur = self.head.next
        while cur:
            if cur.key == key:
                pre.next = cur.next
                return
            pre = cur
            cur = cur.next
            
class MyHashMap:
    def __init__(self):
        self.m = 1009
        self.bucket = [Bucket() for i in range(self.m)]
    def _hash(self, key):
        return key % self.m
    def put(self, key: int, value: int) -> None:
        self.bucket[self._hash(key)].insert(key, value)
    def get(self, key: int) -> int:
        tmp = self.bucket[self._hash(key)].get(key)
        return tmp.val if tmp else -1
    def remove(self, key: int) -> None:
        self.bucket[self._hash(key)].delete(key)
```

### Find First and Last Position of Element in Sorted Array

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums = [float('-inf')] + nums + [float('inf')]
        l, r = 0, len(nums) - 1
        while True:
            mid1 = (l + r) // 2
            if nums[mid1] < target and nums[mid1 + 1] >= target:
                break
            if nums[mid1] == target:
                r = mid1 - 1
                continue
            if nums[mid1] < target:
                l = mid1+1
            else:
                r = mid1-1
        l, r = 0, len(nums) - 1
        while True:
            mid2 = (l + r) // 2
            if nums[mid2] > target and nums[mid2 - 1] <= target:
                break
            if nums[mid2] == target:
                l = mid2 + 1
                continue
            if nums[mid2] < target:
                l = mid2+1
            else:
                r = mid2-1
        if mid2 - mid1 >= 2:
            return [mid1, mid2 - 2]
        else:
            return [-1, -1]
```

### [Factor Combinations](https://leetcode.com/problems/factor-combinations)

```python
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n, res, now, start):
            if now:
                res.append(now + [n])

            for i in range(start, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    dfs(n // i, res, now + [i], i)
            return res
        
        return dfs(n, [], [], 2)
```

### Find K Pairs with Smallest Sums

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = []
        l1, l2 = len(nums1), len(nums2)
        if l1 * l2 != 0:
            heapq.heappush(q, (nums1[0] + nums2[0], 0, 0))
        res = []
        while len(res) < k and q:
            s, i, j = heapq.heappop(q)
            res.append([nums1[i], nums2[j]])
            if i < l1 and j + 1 < l2:
                heapq.heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < l1:
                heapq.heappush(q, (nums1[i + 1] + nums2[0], i + 1, 0))
        return res
```

### Flatten Nested List Iterator

```python
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()
    
    def hasNext(self) -> bool:
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False
```

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

### Insert Delete GetRandom O(1) - Duplicates allowed

```python
class RandomizedCollection:
    def __init__(self):
        self.list = []
        self.dic = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        flag = True if val not in self.dic else False
        self.dic[val].add(len(self.list))
        self.list.append(val)
        return flag

    def remove(self, val: int) -> bool:
        if val in self.dic:
            idx = self.dic[val].pop()
            if (idx + 1) != len(self.list):
                last = self.list[-1]
                self.list[idx] = last
                self.dic[last].remove(len(self.list) - 1)
                self.dic[last].add(idx)
            self.list.pop()
            if not self.dic[val]:
                del self.dic[val]
            return True
        return False

    def getRandom(self) -> int:
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

### [Max Stack](https://leetcode.com/problems/max-stack)

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

###  Minimum Window Substring

```python
class Solution(object):
    def minWindow(self, s, t):
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

### Kth Largest Element in an Array

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        q = []
        for n in nums:
            if len(q) == k:
                heapq.heappush(q, n)
                heapq.heappop(q)
            else:
                heapq.heappush(q, n)
        return min(q)
```

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

### Lowest Common Ancestor of a Binary Tree

```python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q): 
            return root
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
```

### Maximum Depth of Binary Tree

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        res = 0
        while q:
            tq = []
            for n in q:
                if n.left:
                    tq.append(n.left)
                if n.right:
                    tq.append(n.right)
            q = tq
            res += 1
        return res
```

### Max Points on a Line

```python

```

### Maximum Product Subarray

```python
class Solution:
    def solve(self, nums):
        def mul(n):
            return reduce(lambda x, y: x * y, n, 1)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        firstneg, lastneg, numneg = -1, -1, 0
        for i, n in enumerate(nums):
            if n < 0 :
                if firstneg == -1:
                    firstneg = i
                lastneg = i
                numneg += 1
        if numneg % 2 == 0:
            return mul(nums)
        return max(mul(nums[firstneg + 1:]), mul(nums[:lastneg]))
    
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        pre = 0
        for i, n in enumerate(nums):
            if n == 0:
                res = max(res, self.solve(nums[pre: i]))
                pre = i + 1
        res = max(res, self.solve(nums[pre:]))
        return res if pre == 0 else max(res, 0)
```

### Maximum Subarray

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = nums[0]
        for n in nums[1:]:
            cur = max(cur + n, n)
            res = max(res, cur)
        return res
```

### Nested List Weight Sum

```python
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def find(nestedList, depth):
            res = 0
            for i in range(len(nestedList)):
                if nestedList[i].isInteger():
                    res += nestedList[i].getInteger() * depth
                else:
                    res += find(nestedList[i].getList(), depth + 1);
            return res;
                
        return find(nestedList, 1);
```

### [Nested List Weight Sum II](https://leetcode.com/problems/nested-list-weight-sum-ii)

```python
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nest, d):
            for l in nest.getList():
                if l.isInteger():
                    depth.setdefault(d, [])
                    depth[d].append(l.getInteger())
                else:
                    dfs(l, d + 1)
                
        if nestedList == []:
            return 0
            
        depth = {}
        for l in nestedList:
            if l.isInteger():
                depth.setdefault(0, [])
                depth[0].append(l.getInteger())
            else:
                dfs(l, 1)
                
        maxd = max(list(depth.keys()) + [0]) + 1
        res = 0
        for key in depth:
            res += (maxd - key) * sum(depth[key])
        return res  
```

### [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph)

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        res = 0
        visit ={}
        for i in range(n):
            if i not in visit:
                stack = [i]
                visit[i] = True
                res += 1
                while len(stack) > 0:
                    now = stack.pop()
                    for v in dic[now]:
                        if v not in visit:
                            visit[v] = True
                            stack.append(v)
        return res
```

### [Paint House II](https://leetcode.com/problems/paint-house-ii)

```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        min1 = min2 = -1
        for i in range(n):
            last1, last2 = min1, min2
            min1 = min2 = -1
            for j in range(k):
                if j != last1:
                    costs[i][j] += 0 if last1 < 0 else costs[i - 1][last1]
                else:
                    costs[i][j] += 0 if last2 < 0 else costs[i - 1][last2]
                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2, min1 = min1, j
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j
        return costs[n - 1][min1]
```

```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(house_num, color):
            if house_num == n - 1:
                return costs[house_num][color]
            cost = float('inf')
            for next_color in range(k):
                if next_color == color:
                    continue
                cost = min(cost, memo_solve(house_num + 1, next_color))
            return costs[house_num][color] + cost

        n = len(costs)
        if n == 0: return 0
        k = len(costs[0])
        cost = math.inf
        for color in range(k):
            cost = min(cost, memo_solve(0, color))
        return cost
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

### Retain Best Cache

```python
class RetainBestCache:
    def __init__(self, ds, capacity):
        self.cache = {}
        self.rank = defaultdict(set)
        self.rankq = []
        self.capacity = capacity
        self.ds = ds

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        ret = self.ds.get(key)
        cur_rank = self.ds.getrank(key)
        self.cache[key] = ret
        if cur_rank not in self.rank:
            heapq.heappush(self.rankq, cur_rank)
        self.rank[cur_rank].add(key)
        if len(self.cache) > self.capacity:
            self.remove_lowest_rank()
        return ret

    def remove_lowest_rank(self):
        lowest_rank = heapq.heappop(self.rankq)
        keys = self.rank[lowest_rank]
        key = keys.pop()
        del self.cache[key]
        if keys:
            heapq.heappush(self.rankq, lowest_rank)
        else:
            del self.rank[lowest_rank]

class DS:
    def __init__(self):
        self.data = {1: ('A', 1), 2: ('B', 2), 3: ('C', 1), 4: ('D', 2), 5: ('E', 2)}

    def get(self, key):
        return self.data[key][0]

    def getrank(self, key):
        return self.data[key][1]
```

### Second Minimum Node In a Binary Tree

```python
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            dfs(node.left)
            dfs(node.right)
            
        res = [float('inf')]
        dfs(root)
        return -1 if res[0] == float('inf') else res[0]
```

### Serialize and Deserialize Binary Tree

```python
class Codec:
    def serialize(self, root):
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

### Shortest Word Distance II

```pythoon
class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.dict = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.dict[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1 = self.dict[word1]
        l2 = self.dict[word2]
        i = j = 0 
        res = float('inf')
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i]<l2[j]: 
                i += 1 
            else: 
                j += 1
        return res
```

### Symmetric Tree

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def chk(left, right):
            if left and right:
                if left.val == right.val:
                    return chk(left.left, right.right) and chk(left.right, right.left)
            if left == right == None:
                return True
            return False
    
        if root == None:
            return True
        return chk(root.left, root.right)
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

### Valid Perfect Square

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            t = m * m
            if t == num:
                return True
            if t < num:
                l = m + 1
            else:
                r = m - 1
        return False
```

### Valid Parentheses

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {']':'[', ')':'(', '}':'{'}
        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if not stack or stack.pop() != dic[c]:
                    return False
        return stack == []
```

### Valid Parenthesis String

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
                r += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                r -= 1
            else:
                if l > 0:
                    l -= 1
                r += 1
            if r < 0:
                return False
        return l == 0
```

### Valid Triangle Number

```python
class Solution(object):
    def triangleNumber(self, nums):
        if len(nums) <= 2:
            return 0
        nums.sort()
        l = len(nums)
        res = 0
        for i in range(l - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
            
```

thread vs process multithread vs multiprocess
stack memory, heap

db 的 transcation 是怎么支持的

virtual memory


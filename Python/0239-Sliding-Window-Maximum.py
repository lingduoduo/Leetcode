from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que= deque()  # [[i, num]]
        res = []
        for i, num in enumerate(nums):
            if que and i - que[0][0] >= k:
                que.popleft()
            while que and que[-1][-1] <= num:
                que.pop()
            que.append([i, num])
            if i >= k - 1:
                res.append(que[0][1])
        return res


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
    

class MyQueue:  
    def __init__(self):
        self.queue = deque()  

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()  

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):  
            que.push(nums[i])
        result.append(que.front())  
        for i in range(k, len(nums)):
            que.pop(nums[i - k])  
            que.push(nums[i])  
            result.append(que.front())  
        return result


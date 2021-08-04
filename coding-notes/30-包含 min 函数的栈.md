30. 包含 min 函数的栈


题目描述
实现一个包含 min() 函数的栈，该方法返回当前栈中最小的值。

解题思路
使用一个额外的 minStack，栈顶元素为当前栈中最小的值。在对栈进行 push 入栈和 pop 出栈操作时，同样需要对 minStack 进行入栈出栈操作，从而使 minStack 栈顶元素一直为当前栈中最小的值。在进行 push 操作时，需要比较入栈元素和当前栈中最小值，将值较小的元素 push 到 minStack 中。


```java
private Stack<Integer> dataStack = new Stack<>();
private Stack<Integer> minStack = new Stack<>();

public void push(int node) {
    dataStack.push(node);
    minStack.push(minStack.isEmpty() ? node : Math.min(minStack.peek(), node));
}

public void pop() {
    dataStack.pop();
    minStack.pop();
}

public int top() {
    return dataStack.peek();
}

public int min() {
    return minStack.peek();
}
```

```python

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.nums.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            if self.mins[-1] > val:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])
        

    def pop(self) -> None:
        self.mins.pop()
        return self.nums.pop()        

    def top(self) -> int:
        return self.nums[-1]


    def getMin(self) -> int:
        return self.mins[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
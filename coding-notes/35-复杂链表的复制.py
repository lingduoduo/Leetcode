35. 复杂链表的复制


题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的 head。

```java
public class RandomListNode {
    int label;
    RandomListNode next = null;
    RandomListNode random = null;

    RandomListNode(int label) {
        this.label = label;
    }
}
```

解题思路
第一步，在每个节点的后面插入复制的节点。


第二步，对复制节点的 random 链接进行赋值。


第三步，拆分。

```java
public RandomListNode Clone(RandomListNode pHead) {
    if (pHead == null)
        return null;

    // 插入新节点
    RandomListNode cur = pHead;
    while (cur != null) {
        RandomListNode clone = new RandomListNode(cur.label);
        clone.next = cur.next;
        cur.next = clone;
        cur = clone.next;
    }

    // 建立 random 链接
    cur = pHead;
    while (cur != null) {
        RandomListNode clone = cur.next;
        if (cur.random != null)
            clone.random = cur.random.next;
        cur = clone.next;
    }
    
    // 拆分
    cur = pHead;
    RandomListNode pCloneHead = pHead.next;
    while (cur.next != null) {
        RandomListNode next = cur.next;
        cur.next = next.next;
        cur = next;
    }
    return pCloneHead;
}
```

```python
class RandomListNode:
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None

class Solution:
    def clone(self, head):
        if not head:
            return None

        # 插入新节点
        cur = head
        while cur:
            clone = RandomListNode(cur.label)
            clone.next = cur.next 
            cur.next = clone
            cur = clone.next

        # 建立 random 链接
        cur = head
        while cur:
            clone = cur.next
            if cur.random is not None:
                clone.random = cur.random.next
            cur = clone.next

        # 拆分
        cur = head 
        newhead = cur.next
        while cur.next:
            clone = cur.next 
            cur.next = clone.next
            cur = clone
        return newhead

if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.next = RandomListNode(3)
    head.next.next.next = RandomListNode(4)

    head.random = head.next.next
    head.next.next.next.random = head.next
    
    res = Solution().clone(head)
    p = res
    while p:
        print(["next", p.label])
        if p.random:
            print(["random", p.random.label])
        p = p.next
```

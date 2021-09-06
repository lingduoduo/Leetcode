递归

1. 树的高度
104 - Maximum Depth of Binary Tree (Easy)
```java
public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
}
```

```python
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

2. 平衡树
110 Balanced Binary Tree (Easy)

平衡树左右子树高度差都小于等于 1

```java
private boolean result = true;

public boolean isBalanced(TreeNode root) {
    maxDepth(root);
    return result;
}

public int maxDepth(TreeNode root) {
    if (root == null) return 0;
    int l = maxDepth(root.left);
    int r = maxDepth(root.right);
    if (Math.abs(l - r) > 1) result = false;
    return 1 + Math.max(l, r);
}
```

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.maxDepth(root)
        return self.res

    def maxDepth(self, root):
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if abs(l - r) > 1:
            self.res = False
        return 1 + max(l, r)
```

3. 两节点的最长路径
543 Diameter of Binary Tree (Easy)

Input:

         1
        / \
       2  3
      / \
     4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

```java
private int max = 0;

public int diameterOfBinaryTree(TreeNode root) {
    depth(root);
    return max;
}

private int depth(TreeNode root) {
    if (root == null) return 0;
    int leftDepth = depth(root.left);
    int rightDepth = depth(root.right);
    max = Math.max(max, leftDepth + rightDepth);
    return Math.max(leftDepth, rightDepth) + 1;
}
```

```python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.depth(root)
        return self.res

    def depth(self, root):
        if not root:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)

        self.res = max(self.res, l + r)
        
        return 1 + max(l, r)
```
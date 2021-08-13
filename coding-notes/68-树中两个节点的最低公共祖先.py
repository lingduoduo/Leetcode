68. 树中两个节点的最低公共祖先

1 二叉查找树
题目链接
Leetcode : 235. Lowest Common Ancestor of a Binary Search Tree

解题思路
在二叉查找树中，两个节点 p, q 的公共祖先 root 满足 root.val >= p.val && root.val <= q.val。


```java
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null)
        return root;
    if (root.val > p.val && root.val > q.val)
        return lowestCommonAncestor(root.left, p, q);
    if (root.val < p.val && root.val < q.val)
        return lowestCommonAncestor(root.right, p, q);
    return root;
}
```

```
class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root 

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == '__main__':
    root = treeNode(4)
    root.left = treeNode(2)
    root.right = treeNode(6)
    root.left.left = treeNode(1)
    root.left.right = treeNode(3)
    root.right.left = treeNode(5)
    root.right.right = treeNode(7)

    res = Solution().lowestCommonAncestor(root, root.left.left, root.left.right)
    print(res.val)
    ```

2 普通二叉树
题目链接
Leetcode : 236. Lowest Common Ancestor of a Binary Tree

解题思路
在左右子树中查找是否存在 p 或者 q，如果 p 和 q 分别在两个子树中，那么就说明根节点就是最低公共祖先。


```java
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    if (root == null || root == p || root == q)
        return root;
    TreeNode left = lowestCommonAncestor(root.left, p, q);
    TreeNode right = lowestCommonAncestor(root.right, p, q);
    return left == null ? right : right == null ? left : root;
}
```

```python
class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root 
            
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and right:
            return right
        if not right and left:
            return left 
        if left and right:
            return root

if __name__ == '__main__':
    root = treeNode(4)
    root.left = treeNode(2)
    root.right = treeNode(6)
    root.left.left = treeNode(1)
    root.left.right = treeNode(3)
    root.right.left = treeNode(5)
    root.right.right = treeNode(7)

    res = Solution().lowestCommonAncestor(root, root.left.left, root.left.right)
    print(res.val)
```

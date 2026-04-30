from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(node):
            if not node: 
                res.append("#")
                return 
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None

        vals = data.split(",")

        def preorder():      
            val = vals.pop(0)
            if val == "#":
                return None
            
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node

        return preorder(data)


if __name__ == "__main__":
    res = Solution().canSeePersonsCount(heights = [10,6,8,5,11,9])
    print(res)
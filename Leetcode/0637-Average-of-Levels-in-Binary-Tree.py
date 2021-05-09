###Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        sum_list = list()
        cnt_list = list()
        
        def preorder(root, depth):
            if root is None:
                return
            
            if len(sum_list) <= depth:
                sum_list.append(0)
                cnt_list.append(0)
            
            sum_list[depth] += root.val
            cnt_list[depth] += 1
            
            preorder(root.left, depth + 1)
            preorder(root.right, depth + 1)
        
        preorder(root, 0)
        result = [float(s) / n for s, n in zip(sum_list, cnt_list)]
        
        return result


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().averageOfLevels(root)
    print(result)

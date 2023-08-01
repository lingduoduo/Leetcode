from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node, par):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered) or (
                    node.left not in covered or node.right not in covered
                ):
                    self.res += 1
                    covered.update({node, par, node.left, node.right})

        self.res = 0
        covered = {None}
        dfs(root, None)
        return self.res


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 定义递归函数
        result = [0]  # 用于记录摄像头的安装数量
        if self.traversal(root, result) == 0:
            result[0] += 1

        return result[0]


def traversal(self, cur: TreeNode, result: List[int]) -> int:
    if not cur:
        return 2

    left = self.traversal(cur.left, result)
    right = self.traversal(cur.right, result)

    # 情况1: 左右节点都有覆盖
    if left == 2 and right == 2:
        return 0

    # 情况2:
    # left == 0 && right == 0 左右节点无覆盖
    # left == 1 && right == 0 左节点有摄像头，右节点无覆盖
    # left == 0 && right == 1 左节点无覆盖，右节点有摄像头
    # left == 0 && right == 2 左节点无覆盖，右节点覆盖
    # left == 2 && right == 0 左节点覆盖，右节点无覆盖
    elif left == 0 or right == 0:
        result[0] += 1
        return 1

    # 情况3:
    # left == 1 && right == 2 左节点有摄像头，右节点有覆盖
    # left == 2 && right == 1 左节点有覆盖，右节点有摄像头
    # left == 1 && right == 1 左右节点都有摄像头
    else:
        return 2

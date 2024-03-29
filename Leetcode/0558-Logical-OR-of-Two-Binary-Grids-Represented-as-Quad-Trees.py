"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def intersect(self, quadTree1: "Node", quadTree2: "Node") -> "Node":
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        # case2：quadTree1和quadTree2都不是叶节点，深入一层
        else:
            tLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            tRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

            if (
                tLeft.isLeaf
                and tRight.isLeaf
                and bLeft.isLeaf
                and bRight.isLeaf
                and tLeft.val == tRight.val == bLeft.val == bRight.val
            ):
                node = Node(
                    tLeft.val, True, None, None, None, None
                )  # 都是叶节点值都相等，四个叶节点化为一个节点
            else:  # 否则不能化为一个节点
                node = Node(False, False, tLeft, tRight, bLeft, bRight)

        return node

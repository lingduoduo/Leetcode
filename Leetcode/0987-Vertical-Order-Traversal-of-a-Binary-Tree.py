# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.d = collections.defaultdict(list)
        self.dfs(root, 0, 0)

        res = []
        for k in sorted(self.d.keys()):
            level = [val for y, val in sorted(self.d[k], key=lambda x: (-x[0], x[1]))]
            res.append(level)
        return res

    def dfs(self, root, x, y):
        if not root:
            return

        self.d[x].append((y, root.val))

        if root.left:
            self.dfs(root.left, x - 1, y - 1)
        if root.right:
            self.dfs(root.right, x + 1, y - 1)


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = []

        def BFS(root):
            queue = deque([(root, 0, 0)])
            while queue:
                node, row, column = queue.popleft()
                if node is not None:
                    node_list.append((column, row, node.val))
                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). construct the global node list, with the coordinates
        BFS(root)

        # step 2). sort the global node list, according to the coordinates
        node_list.sort()

        # step 3). retrieve the sorted results partitioned by the column index
        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        queue = []
        res = []
        queue.append(root)
        level = 0

        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            level += 1
        return res
                
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(9)

    res = Solution().PrintFromTopToBottom(root)
    print(res)



# ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
#     ArrayList<ArrayList<Integer>> ret = new ArrayList<>();
#     Queue<TreeNode> queue = new LinkedList<>();
#     queue.add(pRoot);
#     while (!queue.isEmpty()) {
#         ArrayList<Integer> list = new ArrayList<>();
#         int cnt = queue.size();
#         while (cnt-- > 0) {
#             TreeNode node = queue.poll();
#             if (node == null)
#                 continue;
#             list.add(node.val);
#             queue.add(node.left);
#             queue.add(node.right);
#         }
#         if (list.size() != 0)
#             ret.add(list);
#     }
#     return ret;
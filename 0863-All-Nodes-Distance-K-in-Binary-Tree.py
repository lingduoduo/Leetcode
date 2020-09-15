###Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution(object):
#     def distanceK(self, root, target, K):
#         """
#         :type root: TreeNode
#         :type target: TreeNode
#         :type K: int
#         :rtype: List[int]
#         """
#         if not root:
#             return None
        
#         self.d = dict()
#         self.buildGraph(None, root)
        
#         ###for k,v in enumerate(self.d):
#         ###    print(k, v.val)
        
#         ###BFS
#         seen = list()
#         seen.append(target)
#         stack = list()
#         stack.append(target)
        
#         k = 0
#         res = []
#         while stack and k <= K:
#             size = len(stack)
#             for i in range(size):
#                 node = stack.pop(0)
#                 if k == K:
#                     res.append(node.val)
                
#                 if node not in self.d:
#                     break
                
#                 for child in self.d[node]:
#                     if child not in seen:
#                         seen.append(child)
#                         stack.append(child)
#             k += 1
#         return res
    
#     def buildGraph(self, parent, child):
#         if parent and child:
#             self.d[parent] = self.d.get(parent, []) + [child]
#             self.d[child] = self.d.get(child, []) + [parent]
        
#         if child.left:
#             self.buildGraph(child, child.left)
        
#         if child.right:
#             self.buildGraph(child, child.right)


        # DFS
        conn = collections.defaultdict(list)
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
            
        connect(None, root)

        # BFS
        bfs = [target.val]
        visited = set([target.val])
        for k in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in visited]
            visited |= set(bfs)
        return bfs

if __name__ == '__main__':
    p = TreeNode(3)
    p.left = TreeNode(5)
    p.right = TreeNode(1)
    p.left.left = TreeNode(6)
    p.left.right = TreeNode(2)
    p.left.right.left = TreeNode(7)
    p.left.right.right = TreeNode(4)
    p.right.right = TreeNode(8)
    
    result = Solution().distanceK(p, p.left, 2)
    print(result)

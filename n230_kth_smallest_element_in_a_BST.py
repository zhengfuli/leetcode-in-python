# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None

        def dfs(root):
            if not root: return

            dfs(root.left)
            print(root.val, k, self.res)
            if not self.k:
                return

            if self.k == 1:
                self.res = root.val
                self.k = 0
                return
            else:
                self.k -= 1
                dfs(root.right)

        dfs(root)
        if self.res is None:
            return root.val
        else:
            return self.res
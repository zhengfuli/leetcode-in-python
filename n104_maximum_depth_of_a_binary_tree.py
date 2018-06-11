# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0

        def dfs(root, depth):
            if not root: return

            self.max_depth = max(self.max_depth, depth+1)

            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        dfs(root, 0)
        return self.max_depth
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0

        def dfs(root, depth):
            if not root: return

            if not root.left and not root.right:
                self.depth = depth if not self.depth else min(self.depth, depth)
                return

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return self.depth
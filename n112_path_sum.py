# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []

        def dfs(root, sum):
            if not root: return

            if not root.left and not root.right: res.append(sum+root.val)

            dfs(root.left, sum + root.val)
            dfs(root.right, sum + root.val)

        dfs(root, 0)
        return True if root and sum in res else False
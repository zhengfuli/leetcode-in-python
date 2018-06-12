# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if left == -1 or right == -1 or abs(left-right) > 1: return -1

            return max(left, right) + 1

        return dfs(root) != -1
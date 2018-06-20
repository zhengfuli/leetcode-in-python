# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(root, sum):
            if not root: return

            if not root.left and not root.right:
                sum = sum * 10 + root.val
                self.res += sum
                return

            if root.val < 0 or root.val > 10:
                return

            dfs(root.left, sum * 10 + root.val)
            dfs(root.right, sum * 10 + root.val)

        dfs(root, 0)
        return self.res
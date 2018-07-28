# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root

        if not root.left and not root.right: return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left

        return root
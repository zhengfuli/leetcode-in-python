# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        depth = 0
        left, right = root, root

        while right:
            left = left.left
            right = right.right
            depth += 1

        if not left:
            return (1 << depth) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
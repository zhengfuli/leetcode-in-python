# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        if not root: return

        parent, left, right = root, root.left, root.right
        if left:
            ret = self.upsideDownBinaryTree(left)
            left.left = right
            left.right = parent
            return ret

        return root


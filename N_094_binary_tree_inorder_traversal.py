# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []

        def dfs(root):
            print(self.res)
            if not root: return
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)

        dfs(root)
        return self.res
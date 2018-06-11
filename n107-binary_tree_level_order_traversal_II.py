# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def dfs(level, root):

            if not root: return

            if len(res) < level: res.append([])

            dfs(level + 1, root.left)
            dfs(level + 1, root.right)

            res[level - 1].append(root.val)

        dfs(1, root)

        return res[::-1]
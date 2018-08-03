# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []

        def dfs(root, path):
            if not root: return

            add = "->" + str(root.val) if path != "" else str(root.val)

            dfs(root.left, path + add)
            dfs(root.right, path + add)

            if not root.left and not root.right: paths.append(path + add)

        dfs(root, "")

        return paths
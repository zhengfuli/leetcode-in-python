# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(start, end):
            if start > end:
                return [None]

            res = []

            for nodeVal in range(start, end + 1):
                leftTrees = dfs(start, nodeVal - 1)
                rightTrees = dfs(nodeVal + 1, end)

                for i in leftTrees:
                    for j in rightTrees:
                        root = TreeNode(nodeVal)
                        root.left, root.right = i, j
                        res.append(root)

            return res

        if not n: return []
        return dfs(1, n)
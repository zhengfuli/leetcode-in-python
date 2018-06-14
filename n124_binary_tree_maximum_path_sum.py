# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            self.max_sum = root.val

        def dfs(root, sum):
            if not root: return 0
            # print(sum, root.val)
            left = dfs(root.left, sum + root.val)
            right = dfs(root.right, sum + root.val)
            # print(sum, root.val, left, right)
            self.max_sum = max(self.max_sum, max(0, sum) + root.val + max(0, left, right), root.val + left + right)

            return max(root.val, root.val + max(left, right))

        dfs(root, 0)
        return self.max_sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.target = sum

        def dfs(stack, root, sum):
            # print(res)
            if not root: return

            if not root.left and not root.right:
                if sum + root.val == self.target:
                    res.append(stack + [root.val])

            stack.append(root.val)
            dfs(stack, root.left, sum + root.val)
            dfs(stack, root.right, sum + root.val)
            stack.pop()

        dfs([], root, 0)
        return res
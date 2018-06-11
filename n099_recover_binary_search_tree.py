# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.swapped1, self.swapped2, self.pre = None, None, None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root: return

            dfs(root.left)

            if self.pre and root.val < self.pre.val:
                if not self.swapped1:
                    self.swapped1, self.swapped2 = self.pre, root
                else:
                    self.swapped2 = root

            self.pre = root

            dfs(root.right)

        dfs(root)

        if self.swapped1 and self.swapped2:
            temp = self.swapped1.val
            self.swapped1.val, self.swapped2.val = self.swapped2.val, temp
        else:
            temp = self.pre.val
            self.swapped2.val, self.pre.val = temp, self.swapped2.val




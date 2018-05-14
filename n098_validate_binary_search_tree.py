# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValid(self, root, min, max):

        if not root or root.val is None:
            return True

        if (min is not None and root.val <= min) or \
           (max is not None and root.val >= max):
            return False

        return self.isValid(root.left, min, root.val) and \
               self.isValid(root.right, root.val, max)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, None, None)

if __name__ == '__main__':
    r = TreeNode(0)
    r.right = TreeNode(-1)

    testBench = Solution()
    print testBench.isValidBST(r)
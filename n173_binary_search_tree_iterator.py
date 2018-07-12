# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        next_smallest = self.stack.pop()
        res = next_smallest.val

        next_smallest = next_smallest.right
        while next_smallest:
            self.stack.append(next_smallest)
            next_smallest = next_smallest.left

        return res

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
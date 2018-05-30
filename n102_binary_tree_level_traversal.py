# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []

        while queue:

            temp = []

            for node in queue:
                queue = queue[1:]

                temp.append(node.val) if node else node

                queue += [node.left, node.right] if node else []

            res.append(temp) if temp else None

        return res

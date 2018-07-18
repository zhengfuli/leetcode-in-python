# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        layered_traversal = []

        def dfs(depth, root):
            if not root: return

            if depth > len(layered_traversal):
                layered_traversal.append([])

            dfs(depth + 1, root.left)
            dfs(depth + 1, root.right)

            layered_traversal[depth - 1].append(root.val)

        dfs(1, root)

        return [layer_nodes[-1] for layer_nodes in layered_traversal]
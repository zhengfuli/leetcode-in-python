# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def dfs(inorder, postorder):
            if not inorder or not postorder: return

            root = TreeNode(postorder[-1])

            if len(inorder) == 1 and len(postorder) == 1 and postorder[0] == inorder[0]: return root

            root.left = dfs(inorder[:inorder.index(postorder[-1])], postorder[:inorder.index(postorder[-1])])

            root.right = dfs(inorder[1+inorder.index(postorder[-1]):], postorder[inorder.index(postorder[-1]):-1])

            return root

        return dfs(inorder, postorder)

if __name__ == '__main__':
    tb = Solution()
    tb.buildTree([9,3,15,20,7], [9,15,7,20,3])
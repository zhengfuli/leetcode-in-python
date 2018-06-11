# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def dfs(preorder, inorder):
            if not preorder or not inorder: return

            root = TreeNode(preorder[0])

            if len(preorder) == 1 and len(inorder) == 1 and preorder[0] == inorder[0]: return root

            root.left = dfs(preorder[1:1+inorder.index(preorder[0])], inorder[:inorder.index(preorder[0])])

            root.right = dfs(preorder[1+inorder.index(preorder[0]):], inorder[inorder.index(preorder[0])+1:])

            return root

        return dfs(preorder, inorder)

if __name__ == '__main__':
    tb = Solution()
    tb.buildTree([1,2], [2,1])
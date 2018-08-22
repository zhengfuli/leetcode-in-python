# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self): self.res = []

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        string = []

        def dfs(root):
            if not root:
                string.append('#')
            else:
                string.append(str(root.val))
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return ' '.join(string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = data.split()

        def level_traversal():
            if queue:
                cur = queue.pop(0)

                if cur == '#': return

                root = TreeNode(int(cur))
                root.left = level_traversal()
                root.right = level_traversal()

                return root

        return level_traversal()
        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
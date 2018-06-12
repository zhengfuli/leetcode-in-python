# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return

        while root:
            cur = root
            while cur:
                print(cur.val)
                if cur.left:
                    if cur.right: cur.left.next = cur.right
                    elif cur.next:
                        temp = cur.next
                        while temp:
                            if temp.left: cur.left.next = temp.left; break
                            elif temp.right: cur.left.next = temp.right; break
                            else: temp = temp.next
                if cur.right:
                    if cur.next:
                        temp = cur.next
                        print(temp.val)
                        while temp:
                            print(temp.val)
                            if temp.left: cur.right.next = temp.left; break
                            elif temp.right: cur.right.next = temp.right; break
                            else: temp = temp.next

                cur = cur.next

            while root and not root.left and not root.right:
                root = root.next

            if root:
                root = root.left if root.left else root.right

def dfs(root):
    if not root: return

    print(root.val)
    if root.next: print(": ", root.next.val)

    dfs(root.left)
    dfs(root.right)

if __name__ == '__main__':
    root = TreeLinkNode(1)
    node_1 = TreeLinkNode(2)
    node_2 = TreeLinkNode(3)
    root.left, root.right = node_1, node_2

    node_3 = TreeLinkNode(4)
    node_4 = TreeLinkNode(5)
    node_2.left, node_2.right = node_3, node_4

    node_5 = TreeLinkNode(7)
    node_6 = TreeLinkNode(8)
    node_3.right = node_5
    node_4.left = node_6

    tb = Solution()
    tb.connect(root)

    dfs(root)

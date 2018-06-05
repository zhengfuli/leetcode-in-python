# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head

        def dfs(start, end):

            if start >= end: return

            mid = int((start + end) / 2)
            left = dfs(start, mid)
            root = TreeNode(self.head.val)
            root.left = left
            self.head = self.head.next
            root.right = dfs(mid+1, end)

            return root

        count = 0
        dummy = head
        while dummy:
            count += 1
            dummy = dummy.next

        return dfs(0, count)
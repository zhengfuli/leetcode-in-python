# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = ListNode(0), ListNode(0)
        fast.next, slow.next = head, head
        stack = []

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)

        while fast.next:
            slow = slow.next
            fast = fast.next

        while slow.next:
            slow = slow.next
            if slow.val != stack.pop():
                return False

        return True
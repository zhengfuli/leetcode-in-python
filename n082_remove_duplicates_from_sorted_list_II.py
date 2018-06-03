# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=head
        while p.next:
            if p.next.val==p.val:
                p.next=p.next.next
            else:
                p=p.next
        return dummy.next
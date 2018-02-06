class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class RotateList(object):
    def rotateList(self, head, k):
        if not head or not head.next:
            return head

        if k <= 0:
            return head

        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1

        if k > length:
            k %= length
            if k == 0:
                k = length
        dummy, tail = head, head

        while k > 0:
            if not tail.next:
                tail = head
                if k == 1:
                    return head
            else:
                tail = tail.next
            k -= 1

        while tail.next:
            dummy = dummy.next
            tail = tail.next

        new_head = dummy.next
        dummy.next = tail.next
        tail.next = head

        return new_head


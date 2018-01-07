import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class MergeKLists(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node != None:
                heap.append((node.val, node))
        heapq.heapify(heap)
        new_head = dummy = ListNode(0)
        while heap:
            popped = heapq.heappop(heap)
            dummy.next = ListNode(popped[0])
            dummy = dummy.next
            if popped[1].next:
                heapq.heappush(heap, (popped[1].next.val, popped[1].next))
        return new_head.next
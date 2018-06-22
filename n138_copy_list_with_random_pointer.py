# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodeMap = {}

        def dfs(node):
            if not node or not node.random: return

            if node in nodeMap: return nodeMap[node]

            clone = RandomListNode(node.label)
            nodeMap[node] = clone

            if node.random in nodeMap:
                clone.random = nodeMap[node.random]
            else:
                clone.random = dfs(node.random)

            if node.next in nodeMap:
                clone.next = nodeMap[node.next]
            else:
                clone.next = dfs(node.next)

            return clone

        dfs(head)
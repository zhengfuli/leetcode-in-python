# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.nodeMap = {}

    def cloneGraph(self, node):
        if not node: return

        root = UndirectedGraphNode(node.label)
        self.nodeMap[node] = root

        for n in node.neighbors:
            if n in self.nodeMap:
                root.neighbors.append(self.nodeMap[n])
            else:
                root.neighbors.append(self.cloneGraph(n))

        return root